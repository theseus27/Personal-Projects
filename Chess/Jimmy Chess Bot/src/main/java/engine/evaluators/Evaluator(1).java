package engine.evaluators;

import chess_rules.Board;

public interface Evaluator {
    int getEvaluation(Board board);
}
