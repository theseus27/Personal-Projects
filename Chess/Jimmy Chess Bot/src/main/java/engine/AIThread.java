package engine;

import chess_rules.Board;
import engine.AIs.AI;

public class AIThread extends Thread {
    private Board board;
    private AI ai;
    private boolean timeToStop;

    private Response bestResponse;

    public AIThread(Board board, AI ai) {
        this.board = board;
        this.ai = ai;
    }

    @Override
    public void run() {
        // System.out.println("Starting thread: " + Thread.currentThread());
        timeToStop = false;
        ai.start();
        if (board.isBoardCheckOrStaleMate() != 0) {
            System.out.println("The AI can't move right now!");
        } else {
            try {
                for (int depth = 1; !timeToStop; depth ++) {
                    setBestResponse(ai.getBestResponse(board, depth));
                }
            } catch (OutOfTimeException ignored) {
            }
        }
        // System.out.println("Stopping thread: " + Thread.currentThread());
    }

    public void finish() {
        timeToStop = true;
        ai.stop();
    }

    public synchronized Response getBestResponse() {
        return bestResponse;
    }

    private synchronized void setBestResponse(Response bestResponse) {
        this.bestResponse = bestResponse;
    }
}
