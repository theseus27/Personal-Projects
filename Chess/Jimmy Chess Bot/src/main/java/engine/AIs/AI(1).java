package engine.AIs;

import chess_rules.Board;
import engine.OutOfTimeException;
import engine.Response;

public interface AI {
    Response getBestResponse(Board board, int depth) throws OutOfTimeException;

    void start();

    void stop();
}
