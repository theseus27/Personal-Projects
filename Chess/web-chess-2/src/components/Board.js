import React, { useState } from "react";
import styles from "../styles/Board.module.css"
import Square from "./Square.js"

function Board() {

  const [selectedSquare, setSelectedSquare] = useState(null);
  const [currentMove, setCurrentMove] = useState([]);
  const [whitesTurn, setWhitesTurn] = useState(true);
  const [errorMessage, setErrorMessage] = useState(null);

  let state = [["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]]
  const gridSize = 8;

  const squareEmpty = (r, c) => {
    if (state[r][c] === "") {
      return true
    }
    return false
  }

  const occupiedByOpponent = (r, c) => {
    if (squareEmpty(r, c)) {
      return false
    }

    if (whitesTurn) {
      if (state[r][c].charAt(0) === 'b') {
        return true
      } else {
        return false
      }
    }
    
    else {
      if (state[r][c].charAt(0) === 'w') {
        return true
      } else {
        return false
      }
    }
  }

  const occupiedBySelf = (r, c) => {
    if (squareEmpty(r, c)) {
      return false
    }

    if (whitesTurn) {
      if (state[r][c].charAt(0) === 'w') {
        return true
      } else {
        return false
      }
    }
    
    else {
      if (state[r][c].charAt(0) === 'b') {
        return true
      } else {
        return false
      }
    } 
  }

  const validateMove = (r1, c1, r2, c2) => {
    // Check that target square doesn't have current player's piece
    if (occupiedBySelf(r2, c2)) {
      setErrorMessage("Invalid selection for move, capturing own piece")
      return false
    }

    // Check that chosen square is a valid move for piece type
    if (state[r1][c1].charAt(1) === 'P') {             // Pawn
      console.log(`Pawn ${r1}, ${c1} to ${r2}, ${c2}`)

      if (whitesTurn) {
        // r1 is 1, r2 is 3, c1==c2, target square is empty and in between square is empty
        if (r1 === 1 && r2 === 3 && c1 === c2 && squareEmpty(r2, c2) && squareEmpty(2, c2)) {
          return true
        }
        // r2 is 1 more than r1, c1==c2, target square is empty
        if (r1 === r2-1 && c1 === c2 && squareEmpty(r2, c2)) {
          return true
        }
        // r2 is 1 more than r1, c1 is 1 more or 1 less than c2, black piece on target square
        if (r1 === r2-1 && c1 === c2+1 && occupiedByOpponent(r2, c2)) {
          return true
        }
        if (r1 === r2-1 && c1 === c2-1 && occupiedByOpponent(r2, c2)) {
          return true
        }
        return false
      } else {
        // r1 is 6, r2 is 4, c1==c2, target square is empty and in between square is empty
        if (r1 === 6 && r2 === 4 && c1 === c2 && squareEmpty(r2, c2) && squareEmpty(5, c2)) {
          return true
        }
        // r2 is 1 less than r1, c1==c2, target square is empty
        if (r1 === r2+1 && c1 === c2 && squareEmpty(r2, c2)) {
          return true
        }
        // r2 is 1 less than r1, c1 is 1 more or 1 less than c2, white piece on target square
        if (r1 === r2+1 && c1 === c2+1 && occupiedByOpponent(r2, c2)) {
          return true
        }
        if (r1 === r2+1 && c1 === c2-1 && occupiedByOpponent(r2, c2)) {
          return true
        }
        return false
      }

    } else if (state[r1][c1].charAt(1) === 'R') {      // Rook TODO
      // r1 === r2 and for everything in between c1 and c2, every square is empty
      
      // c1 === c2 and for everything in between r1 and r2, every square is empty
    } else if (state[r1][c1].charAt(1) === 'B') {      // Bishop TODO
      // |c2-c1| === |r2-r1|
    } else if (state[r1][c1].charAt(1) === 'Q') {      // Queen TODO
      // Rook or bishop logic
    } else if (state[r1][c1].charAt(1) === 'K') {      // King
      // Check 1 square in every direction
      if (Math.abs(r2-r1) === 1 && Math.abs(c2-c1) < 2) {
        return true
      }
      if (Math.abs(c2-c1) === 1 && Math.abs(r2-r1) < 2) {
        return true
      }
      return false
    } else if (state[r1][c1].charAt(1) === 'N') {      // Knight
      // Check |r2-r1| === 2 and |c2-c1| === 1
      if (Math.abs(r2-r1) === 2 && Math.abs(c2-c1) === 1) {
        return true
      }
      // Or |r2-r1| === 1 and |c2-c1| === 2
      if (Math.abs(r2-r1) === 1 && Math.abs(c2-c1) === 2) {
        return true
      }
      return false
    } else {
      setErrorMessage("Selected piece is not valid piece type")
      return false
    }
  }

  const selectSquare = (row, col) => {
    // White
    if (whitesTurn) {
      // Check that selected square has a piece of the current person's color
      if (state[row][col] === "" || state[row][col].charAt(0) !== 'w') {
        setErrorMessage("Invalid selection for white")
      } else {
        setSelectedSquare({ row, col });
        setErrorMessage(null)
        // console.log(`Selecting ${rowcolToChess(row, col)}`)
      }
    }

    // Black
    else {
      if (state[row][col] === "" || state[row][col].charAt(0) !== 'b') {
        setErrorMessage("Invalid selection for black")
      } else {
        setSelectedSquare({ row, col });
        setErrorMessage(null)
      }
    } 
  }

  const handleClick = (row, col) => {
    // console.log(`${rowcolToChess(row, col)} was clicked`);

    // Set the selected square
    if (selectedSquare === null) {
      selectSquare(row, col)
    } 
    else {
      //Deselect Square
      if (row === selectedSquare.row && col === selectedSquare.col) {
        console.log(`Deselecting ${rowcolToChess(row, col)}`)
        setErrorMessage(null)
        setSelectedSquare(null);
      } 
      // Make Move
      else {
        if (validateMove(selectedSquare.row, selectedSquare.col, row, col)) {
            // Check that you're not opening up a check
            // Check that you're not in check and not moving out of it
          const move = { from: selectedSquare, to: { row, col } };
          setCurrentMove([...currentMove, move]);
          console.log(`Moving from ${rowcolToChess(selectedSquare.row, selectedSquare.col)} to ${rowcolToChess(row, col)}`)
          setSelectedSquare(null);
          setWhitesTurn(!whitesTurn)
        } else {
          setErrorMessage("Invalid Move")
        }
      }
    }
  };

  const rowcolToChess = (row, col) => {
    let rank = (row+1).toString()
    let file = 'a'
    switch (col) {
      case 0: 
        file = 'a';
        break;
      case 1:
        file = 'b';
        break;
      case 2:
        file = 'c';
        break;
      case 3:
        file = 'd';
        break; 
      case 4:
        file = 'e';
        break;
      case 5:
        file = 'f';
        break;
      case 6:
        file = 'g';
        break;
      case 7:
        file = 'h';
        break;
      default:
        file = "other";
        break;
    }

    return file.toString().concat(rank)

  };

  const renderSquares = () => {
    const cells = [];
    for (let i = 0; i < gridSize; i++) {
      for (let j = 0; j < gridSize; j++) {
        const isHighlighted = selectedSquare && selectedSquare.row === 7-i && selectedSquare.col === j;
          cells.push(<Square 
                        piece={state[7-i][j]} 
                        rank={7-i} 
                        file={j}
                        onClick={() => handleClick(7-i, j)}
                        isHighlighted={isHighlighted}/>)
      }
    }
    // cells.push(<div key={i} className={styles.square}></div>);

    return (
      <div className={styles.board}>
        {cells}
      </div>
    );
  }

  return (
    <div className="chessboard" style={{"display":"flex", "flexDirection":"column"}}>
      <h2>Chess</h2>
      <h3 style={{"color":"red", "marginTop":"5vmin"}}>Error Field: {errorMessage}</h3>

      <div className="board" style={{"width":"70%"}}>
        {renderSquares()}
      </div>

      <div style={{"width":"30%"}}>
        <h3>Current Move</h3>
        {currentMove.map((move, index) => (
          <div key={index}>
            Move {index + 1}: From ({move.from.row}, {move.from.col}) to ({move.to.row}, {move.to.col})
          </div>
        ))}
      </div>
    </div>
  );
}

export default Board;