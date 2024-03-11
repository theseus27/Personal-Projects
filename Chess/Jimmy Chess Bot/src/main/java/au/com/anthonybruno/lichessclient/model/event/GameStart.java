package au.com.anthonybruno.lichessclient.model.event;

import com.fasterxml.jackson.annotation.JsonProperty;

public class GameStart {

    private final String type;
    private final Game game;

    public GameStart(@JsonProperty("type") String type, @JsonProperty("game") Game game) {
        this.type = type;
        this.game = game;
    }

    public String getId() {
        return game.getId();
    }

    @Override
    public String toString() {
        return "GameStart{" +
                "type='" + type + '\'' +
                ", gameId=" + game.getId() +
                '}';
    }

    private static class Game {

        private final String id;

        private Game(@JsonProperty("id") String id) {
            this.id = id;
        }

        public String getId() {
            return id;
        }
    }
}
