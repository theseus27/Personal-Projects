package au.com.anthonybruno.lichessclient.handler;


import au.com.anthonybruno.lichessclient.model.event.GameStart;
import com.fasterxml.jackson.databind.node.ObjectNode;

public interface UserEventHandler {

    void incomingChallenge(ObjectNode challengeEvent);

    void gameStart(GameStart gameStartEvent);
}
