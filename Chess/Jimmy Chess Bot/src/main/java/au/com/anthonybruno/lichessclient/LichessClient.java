package au.com.anthonybruno.lichessclient;


import au.com.anthonybruno.lichessclient.handler.GameEventHandler;
import au.com.anthonybruno.lichessclient.handler.UserEventHandler;
import au.com.anthonybruno.lichessclient.http.Json;
import au.com.anthonybruno.lichessclient.http.JsonClient;
import au.com.anthonybruno.lichessclient.http.JsonResponse;
import au.com.anthonybruno.lichessclient.model.Status;
import au.com.anthonybruno.lichessclient.model.account.Email;
import au.com.anthonybruno.lichessclient.model.account.KidModeStatus;
import au.com.anthonybruno.lichessclient.model.event.GameStart;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.http.Header;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.message.BasicHeader;

import java.net.URISyntaxException;
import java.util.Collections;
import java.util.List;

public class LichessClient implements AutoCloseable {

    public static final String BASE_URL = "https://lichess.org";
    private final JsonClient httpClient;

    public LichessClient(String apiToken) {
        List<Header> defaultHeaders = Collections.singletonList(new BasicHeader("Authorization", "Bearer " + apiToken));
        this.httpClient = new JsonClient(HttpClientBuilder.create().setDefaultHeaders(defaultHeaders).build());
    }

    public ObjectNode getMyProfile() {
        return (ObjectNode) get(URLS.ACCOUNT.toString());
    }

    public String getMyEmailAddress() {
        return get(URLS.ACCOUNT + "/email", Email.class).getEmail();
    }

    public ObjectNode getMyPreferences() {
        return (ObjectNode) get(URLS.ACCOUNT + "/preferences");
    }

    public boolean getMyKidModeStatus() {
        return get(URLS.ACCOUNT + "/kid", KidModeStatus.class).isOn();
    }

    public Status setMyKidModeStatus(boolean status) {
        String url;
        try {
            url = new URIBuilder(URLS.ACCOUNT + "/kid").addParameter("v", status + "").build().toString();
        } catch (URISyntaxException e) {
            throw new RuntimeException(e);
        }
        return post(url, Status.class);
    }

    public Status upgradeToBotAccount() {
        return post(URLS.BOT + "/account/upgrade", Status.class);
    }

    public void streamIncomingEvents(UserEventHandler handler) {
        httpClient.getAndStream(URLS.STREAM + "/event", (json, context) -> {
            ObjectNode node = (ObjectNode) json;
            String type = node.get("type").asText();
            if (type.equals("challenge")) {
                handler.incomingChallenge(node);
            } else if (type.equals("gameStart")) {
                handler.gameStart(Json.parseJson(node, GameStart.class));
            } else {
                throw new RuntimeException("Unhandled event type: '" + type + "' \nFull json: " + json);
            }
        });
    }

    public void streamGameState(String gameId, GameEventHandler handler) {
        httpClient.getAndStream(URLS.BOT + "/game/stream/" + gameId, (json, context) -> {
            ObjectNode node = (ObjectNode) json;
            String type = node.get("type").asText();
            if (type.equals("gameFull")) {
                handler.fullGameState(node);
            } else if (type.equals("gameState")) {
                handler.gameStateUpdate(node);
            } else if (type.equals("chatLine")) {
                handler.chatReceived(node);
            }

        });
    }

    public Status makeMove(String gameId, String move) {
        String url = URLS.BOT + "/game/" + gameId + "/move/" + move;
        return post(url, Status.class);
    }

    public Status writeInChat(String gameId, String room, String message) {
        String url = URLS.BOT + "/game/" + gameId + "/chat";
        ObjectNode json = Json.createJsonObject();
        json.put("room", room);
        json.put("text", message);
        return post(url, json, Status.class);
    }


    public Status abortGame(String gameId) {
        String url = URLS.BOT + "/game/" + gameId + "/abort";
        return post(url, Status.class);
    }

    public Status resignGame(String gameId) {
        String url = URLS.BOT + "/game/" + gameId + "/resign";
        return post(url, Status.class);
    }

    public Status acceptChallenge(String challengeId) {
        return post(URLS.CHALLENGE + "/" + challengeId + "/accept", Status.class);
    }

    public Status declineChallenge(String challengeId) {
        return post(URLS.CHALLENGE + "/" + challengeId + "/decline", Status.class);
    }

    public ObjectNode getMembersOfTeam(String teamId, Integer max) {
        String url;
        try {
            URIBuilder uriBuilder = new URIBuilder(URLS.TEAM + "/" + teamId + "/users");
            if (max != null) {
                uriBuilder.addParameter("max", String.valueOf(max));
            }
            url = uriBuilder.build().toString();
        } catch (URISyntaxException e) {
            throw new RuntimeException(e);
        }
        return (ObjectNode) get(url);
    }

    public ObjectNode getCurrentTournaments() {
        return (ObjectNode) get(URLS.TOURNAMENT.toString());
    }

    public void createChallenge(String username, boolean rated) {
        String url = URLS.CHALLENGE + "/" + username;
        ObjectNode json = Json.createJsonObject();
        json.put("rated", rated);
        post(url, json, Status.class);
    }

    private JsonNode get(String url) {
        try (JsonResponse response = httpClient.get(url)) {
            return response.toJson();
        }
    }

    private <T> T get(String url, Class<T> toConvertTo) {
        try (JsonResponse response = httpClient.get(url)) {
            return response.toObject(toConvertTo);
        }
    }

    private <T> T post(String url, Class<T> toConvertTo) {
        try (JsonResponse response = httpClient.post(url)) {
            return response.toObject(toConvertTo);
        }
    }

    private <T> T post(String url, ObjectNode postData, Class<T> toConvertTo) {
        try (JsonResponse response = httpClient.post(url, postData)) {
            return response.toObject(toConvertTo);
        }
    }

    @Override
    public void close() throws Exception {
        httpClient.close();
    }

}
