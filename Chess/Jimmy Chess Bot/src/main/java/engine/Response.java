package engine;

import chess_rules.Move;
import java.util.ArrayList;

public class Response {
    private ArrayList<Move> moveList;
    private int resultingEvaluation;

    public Response() {
        moveList = new ArrayList<>();
    }

    public void addMove(Move move) {
        moveList.add(move);
    }

    public ArrayList<Move> getMoveList() {
        return moveList;
    }

    public Move getMove(int location) {
        return moveList.get(location);
    }

    public void setResultingEvaluation(int resultingEvaluation) {
        this.resultingEvaluation = resultingEvaluation;
    }

    public int getResultingEvaluation() {
        return resultingEvaluation;
    }
}
