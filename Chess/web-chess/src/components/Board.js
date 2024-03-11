import React from "react";
import styles from "../styles/Board.module.css"
import Square from "./Square.js"

class Board extends React.Component {
  render() {
    const state = [["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]]
    const gridSize = 8;

    const cells = [];
    for (let i = 0; i < gridSize; i++) {
      for (let j = 0; j < gridSize; j++) {
          cells.push(<Square piece={state[7-i][j]} rank={7-i} file={j}/>)
      }
    }
    // cells.push(<div key={i} className={styles.square}></div>);


    return (
      <div className={styles.board}>
        {cells}
      </div>
    );
  }
}

export default Board;