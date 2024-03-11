import React from "react";
import styles from "../styles/Square.module.css";

import WhitePawn from "../images/whitepawn.png";
import WhiteRook from "../images/whiterook.png";
import WhiteBishop from "../images/whitebishop.png";
import WhiteKnight from "../images/whiteknight.png";
import WhiteKing from "../images/whiteking.png";
import WhiteQueen from "../images/whitequeen.png";

import BlackPawn from "../images/blackpawn.png";
import BlackRook from "../images/blackrook.png";
import BlackBishop from "../images/blackbishop.png";
import BlackKnight from "../images/blackknight.png";
import BlackKing from "../images/blackking.png";
import BlackQueen from "../images/blackqueen.png";

import QuestionMark from "../images/questionmark.jpg"

function getPicture(piece) {
  switch (piece) {
    case "wR": return WhiteRook;
    case "wN": return WhiteKnight;
    case "wB": return WhiteBishop;
    case "wP": return WhitePawn;
    case "wQ": return WhiteQueen;
    case "wK": return WhiteKing;

    case "bR": return BlackRook;
    case "bN": return BlackKnight;
    case "bB": return BlackBishop;
    case "bP": return BlackPawn;
    case "bQ": return BlackQueen;
    case "bK": return BlackKing;

    default: return QuestionMark;
  }
}

function Square(props) {
  let color = "black"
  if ((props.rank % 2 === 0 && props.file % 2 === 1) || (props.rank % 2 === 1 && props.file % 2 === 0)) {
    color = "white"
  }

  const borderStyle = {border: props.isHighlighted ? '5px solid blue' : '5px solid transparent'}

  return (
    <div className={color==="black" ? styles.blackSquare : styles.whiteSquare} onClick={props.onClick} style={borderStyle}>
      {props.piece === "" ? <p></p> : <img src={getPicture(props.piece)} alt={props.piece} width="30px" height="50px"/>}

      {/* <p>{props.rank}, {props.file}</p> */}
    </div>
  )
}

export default Square;
