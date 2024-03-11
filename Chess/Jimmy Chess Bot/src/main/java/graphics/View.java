package graphics;/*
 * Author: Jimmy Maslen
 * I used Andrew Merrill's "MineView" class as sort of a template to write this
 */

import chess_rules.Board;
import chess_rules.Game;
import chess_rules.Move;
import chess_rules.Square;
import engine.AIThread;
import engine.AIs.AI;
import engine.Response;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.ArrayList;

class View {

    private Game game;
    private AI ai;
    private Image[][] pieceImages;
    private JFrame mainFrame;
    private GamePanel gamePanel;
    private ControlPanel controlPanel;
    private MyMenuBar menuBar;
    private boolean compIsWhite;
    private boolean compIsBlack;
    private boolean displaySequence;
    private long aiTimeLimit;

    // Threads
    private SequenceUpdaterThread sequenceUpdaterThread = new SequenceUpdaterThread();
    private AIThread aiThread;

    View(AI ai, boolean compIsWhite, boolean compIsBlack, int width, int height, long aiTimeLimit) {
        this.game = new Game();
        this.compIsWhite = compIsWhite;
        this.compIsBlack = compIsBlack;
        displaySequence = !compIsWhite && !compIsBlack;
        this.aiTimeLimit = aiTimeLimit;
        this.ai = ai;
        aiThread = new AIThread(game.currentBoard.copy(), ai);

        pieceImages = new BufferedImage[2][6];
        for (int color = 0; color < pieceImages.length; color ++) {
            for (int piece = 0; piece < pieceImages[color].length; piece++) {
                Image pieceImage = new BufferedImage(1, 1 , BufferedImage.TYPE_3BYTE_BGR);
                try {
                    String fileName = "PieceImages/" + (2 * color - 1 + "_" + (piece + 1) + ".png");
                    pieceImage = ImageIO.read(new File(fileName));
                } catch (Exception e) {
                    e.printStackTrace();
                }
                pieceImages[color][piece] = pieceImage;
            }
        }

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        gamePanel = new GamePanel();
        controlPanel = new ControlPanel();
        mainPanel.add(gamePanel, BorderLayout.CENTER);
        mainPanel.add(controlPanel, BorderLayout.SOUTH);
        mainFrame = new JFrame("Chess");
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.getContentPane().add(mainPanel);
        mainFrame.setSize(width, height);
        mainFrame.setLocationRelativeTo(null);
        mainFrame.setVisible(true);
        menuBar = new MyMenuBar();
        mainFrame.setJMenuBar(menuBar);
    }

    private void repaintGamePanel() {
        gamePanel.repaint();
    }

    private void displayGameEndStatement() {
        if (game.isGameOver() == 1) {
            JOptionPane.showMessageDialog(mainFrame, "Game is a draw!");
        } else if (game.isGameOver() == 2) {
            JOptionPane.showMessageDialog(mainFrame, "Game has been won by white!");
        } else if (game.isGameOver() == 3) {
            JOptionPane.showMessageDialog(mainFrame, "Game has been won by black!");
        }
    }

    private void startNewGame() {
        game.startNewGame();
        repaintGamePanel();
        displaySequence = !compIsWhite && !compIsBlack;
        if (game.isAITurn(compIsWhite, compIsBlack)) {
            startAI();
        }
        aiThread = new AIThread(game.currentBoard.copy(), ai);
        runAI();
    }

    private void movePiece(Move move) {

        game.move(move);
        repaintGamePanel();

        aiThread.finish();
        try {
            aiThread.join();
        } catch (InterruptedException ignored) {}
        aiThread = new AIThread(game.currentBoard.copy(), ai);
        runAI();
    }

    private void runAI() {
        // TODO: Turn back on
        if (game.isAITurn(compIsWhite, compIsBlack) || (!compIsWhite && !compIsBlack)) {
            aiThread.start();
        }

        sequenceUpdaterThread.finish();
        if (displaySequence) {
            calculateAndDisplaySequence();
        } else {
            controlPanel.setSequenceLabel("Disabled (Computer is Playing)");

        }
        if (game.isAITurn(compIsWhite, compIsBlack)) {
            startAI();
        }
    }

    private void startAI() {
        Thread aiPLayingThread = new aiPlayingThread();
        aiPLayingThread.start();
    }

    private void calculateAndDisplaySequence() {
        sequenceUpdaterThread = new SequenceUpdaterThread();
        sequenceUpdaterThread.start();
    }

    /////////////////////////////////////////////////////////////////////////////////////////
    /* The ControlPanel is the panel with the New Game button, the outputs of the AI, and game timer. */
    class ControlPanel extends JPanel {
        private JLabel evaluationLabel, sequenceLabel, timeLabel;
        private javax.swing.Timer timer;

        ControlPanel() {
            setLayout(new FlowLayout());

            // TODO: Add this to the upper place thing
            JButton newGameButton = new JButton("New Game");
            newGameButton.addActionListener(new NewGameListener());
            newGameButton.setMnemonic(KeyEvent.VK_N);
            add(newGameButton);
            /////////////////////////////////////

            add(new JLabel("Evaluation: "));
            evaluationLabel = new JLabel("0.0    ");
            add(evaluationLabel);
            add(new JLabel("Sequence: "));
            sequenceLabel = new JLabel("    ");
            add(sequenceLabel);
//            timeLabel = new JLabel(" 0:00");
//            add(new JLabel("Time: "));
//            add(timeLabel);

//            timer = new javax.swing.Timer(100, new TimerListener());
//            timer.start();
        }

        /////////////////////////////////////////////////////////////////////////////////////////
        /** NewGameListener is used when the New Game button is clicked. */

        class NewGameListener implements ActionListener {
            public void actionPerformed(ActionEvent event) {
                startNewGame();
            }
        }  // class NewGameListener

        void updateEvaluation(int evaluation) {
            evaluationLabel.setText(Integer.toString(evaluation));
        }

        void setNonEvaluation() {
            evaluationLabel.setText("n/a");
        }

        void updateSequence(ArrayList<Move> sequence) {
            StringBuilder sequenceString = new StringBuilder();
            for (Move move: sequence) {
                sequenceString.append(move.toString()).append(", ");
            }
            sequenceLabel.setText(sequenceString.toString());
        }

        void setSequenceLabel(String s) {
            sequenceLabel.setText(s);
        }

        /////////////////////////////////////////////////////////////////////////////////////////
        /** The timer is used to update the display of the current time and the number of flags placed. */
        // TODO: put this

//        class TimerListener implements ActionListener {
//            private java.text.DecimalFormat twoDigitFormat = new java.text.DecimalFormat("00");
//
//            public void actionPerformed(ActionEvent event) {
//
//            }
//        }


    } // class ControlPanel

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    /* The GamePanel is where the field is drawn on the screen. */
    private class GamePanel extends JPanel {
        private int panelHeight, panelWidth;  // size of the entire game panel
        private int squareLength;      // size of each cell
        private int offsetX, offsetY;         // offset between the northwest corner of the panel
        // and the northwest corner of the upper-left cell
        private Square currentSquare;
        private ArrayList<Move> currentPossibleMoves = new ArrayList<>();

        GamePanel() {
            addMouseListener(new MineMouseListener());
            addComponentListener(new GamePanelComponentListener());
        }

        /*
        // TODO: calculate based on size of screen
         */
        void calculateSquareSize() {
            Dimension d = getSize();
            panelWidth = d.width;
            panelHeight = d.height;

            int boardSide;
            if (panelWidth < panelHeight) {
                boardSide = panelWidth;
                offsetX = 0;
                offsetY = (panelHeight - panelWidth) / 2;
            } else {
                boardSide = panelHeight;
                offsetX = (panelWidth - panelHeight) / 2;
                offsetY = 0;
            }

            squareLength = boardSide / 8;
        }

        /* paintComponent re-draws the field */

        protected void paintComponent(Graphics pen) {
            // make the background black
            pen.setColor(Color.BLACK);
            pen.fillRect(0, 0, panelWidth, panelHeight);

            int numRows = 8;
            int numCols = 8;

            // draw every cell
            for (int r=0; r<numRows; r++) {
                for (int c=0; c<numCols; c++) {
                    Square square = game.currentBoard.getSquare(r, c);
                    drawSquare(pen, square);
                }
            }
        } // paintComponent()

        private void drawSquare(Graphics pen, Square square) {
            // compute x and y coordinates of the north-west corner of the cell
            int nw_x = square.getCol() * squareLength + offsetX;
            int nw_y = square.getRow() * squareLength + offsetY;

            // draw a border around the cell
            pen.setColor(Color.BLACK);
            pen.drawRect(nw_x, nw_y, squareLength, squareLength);

            if (square.isHighlighted) {
                pen.setColor(Color.YELLOW);
            } else if (square.isPossibleMove) {
                pen.setColor(Color.ORANGE);
            } else if ((square.getCol() + square.getRow()) % 2 == 0) {
                pen.setColor(Color.WHITE);
            } else {
                pen.setColor(Color.GREEN);
            }
            pen.fillRect(nw_x+1, nw_y+1, squareLength-2, squareLength-2);

            if (square.pieceID > 0) {
                Image pieceImage = pieceImages[(square.pieceColor + 1)/2][square.pieceID - 1];
                pen.drawImage(pieceImage, nw_x, nw_y, squareLength, squareLength, this);
            }
        }

        private Square getSquare(int x, int y) {
            int col = (x-offsetX)/squareLength;
            int row = (y-offsetY)/squareLength;
            if (Board.isLegalCoordinate(col) && Board.isLegalCoordinate(row)) {
                return game.currentBoard.getSquare(row, col);
            }
            return null;
        }

        /////////////////////////////////////////////////////////////////////////////////////////

        class MineMouseListener implements MouseListener {
            public void mousePressed(MouseEvent event) {

                // Boolean solution
                //boolean pieceMoved = false;

                Square pressedSquare = getSquare(event.getX(), event.getY());

                if (!game.isGameOver && game.hasGameStarted && !(game.currentBoard.getTurn() == -1 && compIsWhite) && !(game.currentBoard.getTurn() == 1 && compIsBlack)) {
                    if (pressedSquare != null && pressedSquare.isPossibleMove) {
                        Move currentMove = null;
                        for (Move move: currentPossibleMoves) {
                            if (currentSquare.getRow() == move.getStartRow() && currentSquare.getCol() == move.getStartCol() && pressedSquare.getRow() == move.getEndRow() && pressedSquare.getCol() == move.getEndCol()) {
                                currentMove = move;
                            }
                        }
                        movePiece(currentMove);

                        //pieceMoved = true;
                        currentSquare.isHighlighted = false;
                        currentSquare = null;
                        for (Move move : currentPossibleMoves) {
                            Square endSquare = game.currentBoard.getSquare(move.getEndRow(), move.getEndCol());
                            endSquare.isPossibleMove = false;
                        }
                        currentPossibleMoves.clear();

                        // Start new thread if comp should play

                        if ((game.currentBoard.getTurn() == Board.WHITE && compIsWhite) || (game.currentBoard.getTurn() == Board.BLACK && compIsBlack)) {
                            startAI();
                        }
                    } else {
                        if (currentSquare != null) {
                            currentSquare.isHighlighted = false;
                        }
                        for (Move move : currentPossibleMoves) {
                            Square endSquare = game.currentBoard.getSquare(move.getEndRow(), move.getEndCol());
                            endSquare.isPossibleMove = false;
                        }
                        currentSquare = pressedSquare;
                        if (pressedSquare != null) {
                            pressedSquare.isHighlighted = true;
                        }
                        currentPossibleMoves.clear();
                        currentPossibleMoves.addAll(game.currentBoard.getPossibleMoves(currentSquare));
                        for (Move move : currentPossibleMoves) {
                            Square endSquare = game.currentBoard.getSquare(move.getEndRow(), move.getEndCol());
                            endSquare.isPossibleMove = true;
                        }
                    }
                    if (game.isGameOver() != 0) {
                        displayGameEndStatement();
                    }
                }

                repaint();
            }
            public void mouseClicked(MouseEvent event) { }
            public void mouseReleased(MouseEvent event) { }
            public void mouseEntered(MouseEvent event) { }
            public void mouseExited(MouseEvent event) { }
        }  // class MineMouseListener

        //////////////////////////////////////////////////////////////////////////////////////////

        class GamePanelComponentListener extends ComponentAdapter {
            public void componentResized(ComponentEvent event) {
                // when the game panel is resized, adjust the size of the cells
                calculateSquareSize();
                repaint();
            }
        } // class GamePanelComponentListener

        /////////////////////////////////////////////////////////////////////////////////////////

    } // class GamePanel

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////
    class MyMenuBar extends JMenuBar {
        MyMenuBar() {
            add(new FileMenu());
        }

        class FileMenu extends JMenu {
            FileMenu() {
                super("File");
                add(new NewMenu());
                add(new OpenMenuItem());
                add(new SaveMenuItem());
            }

            class NewMenu extends JMenu {
                NewMenu() {
                    super("New Game");
                    add(new CompDisabled());
                    add(new CompPlaysWhite());
                    add(new CompPlaysBlack());
                    add(new CompPlaysBoth());
                }

                public class CompDisabled extends JMenuItem implements ActionListener {
                    CompDisabled() {
                        super("Computer Disabled");
                        addActionListener(this);
                    }

                    public void actionPerformed(ActionEvent e) {
                        compIsWhite = false;
                        compIsBlack = false;
                        startNewGame();
                    }
                }

                public class CompPlaysWhite extends JMenuItem implements ActionListener {
                    CompPlaysWhite() {
                        super("Computer Plays White");
                        addActionListener(this);
                    }

                    public void actionPerformed(ActionEvent e) {
                        compIsWhite = true;
                        compIsBlack = false;
                        startNewGame();
                    }
                }

                public class CompPlaysBlack extends JMenuItem implements ActionListener {
                    CompPlaysBlack() {
                        super("Computer Plays Black");
                        addActionListener(this);
                    }

                    public void actionPerformed(ActionEvent e) {
                        game.currentBoard.newGame();
                        repaintGamePanel();

                        compIsWhite = false;
                        compIsBlack = true;
                        startNewGame();
                    }
                }

                public class CompPlaysBoth extends JMenuItem implements ActionListener {
                    CompPlaysBoth() {
                        super("Computer Plays Both");
                        addActionListener(this);
                    }

                    public void actionPerformed(ActionEvent e) {
                        compIsWhite = true;
                        compIsBlack = true;
                        startNewGame();
                    }
                }

            }

            public class OpenMenuItem extends JMenuItem implements ActionListener {
                OpenMenuItem() {
                    super("Open");
                    addActionListener(this);
                }

                public void actionPerformed(ActionEvent e) {
                    // TODO: do this later
                }
            }

            public class SaveMenuItem extends JMenuItem implements ActionListener {
                SaveMenuItem() {
                    super("Save");
                    addActionListener(this);
                }

                public void actionPerformed(ActionEvent e) {
                    // TODO: do this later
                }

            }
        }
    }

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    class SequenceUpdaterThread extends Thread {
        boolean timeToStop;

        @Override
        public void run(){
            timeToStop = false;

            while (!timeToStop) {
                try {
                    Thread.sleep(100);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                Response bestResponse = aiThread.getBestResponse();
                if (bestResponse != null) {
                    StringBuilder responseString = new StringBuilder();
                    for (Move move: bestResponse.getMoveList()) {
                        responseString.append(move).append(", ");
                    }
                    controlPanel.setSequenceLabel(responseString.toString());
                    controlPanel.updateEvaluation(bestResponse.getResultingEvaluation());
                    repaintGamePanel();
                }
            }
            // controlPanel.updateEvaluation(new CPWEval().getEvaluation(game.currentBoard.copy()));
        }

        void finish() {
            timeToStop = true;
        }
    }

    class aiPlayingThread extends Thread {
        @Override
        public void run() {
            try {
                Thread.sleep(aiTimeLimit);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            Response bestResponse = aiThread.getBestResponse();
            while (bestResponse == null) {
                try {
                    Thread.sleep(aiTimeLimit);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                bestResponse = aiThread.getBestResponse();
            }
            movePiece(bestResponse.getMove(0));
            repaintGamePanel();
        }
    }

}
