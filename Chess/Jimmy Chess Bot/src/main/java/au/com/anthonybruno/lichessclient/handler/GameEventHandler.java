package au.com.anthonybruno.lichessclient.handler;


import com.fasterxml.jackson.databind.node.ObjectNode;

public interface GameEventHandler {

    void chatReceived(ObjectNode chat);

    void fullGameState(ObjectNode gameState);

    void gameStateUpdate(ObjectNode gameState);
}
