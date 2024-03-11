import React from "react";
import styles from "../styles/Square.module.css";
import Image from "next/image";

function Square(props) {
  let color = "black"
  if ((props.rank % 2 === 0 && props.file % 2 === 1) || (props.rank % 2 === 1 && props.file % 2 === 0)) {
    color = "white"
  }

  return (
    <div className={color==="black" ? styles.blackSquare : styles.whiteSquare}>
      {props.piece === "" ? <Image></Image> : <p></p>}

      {/* <p>{props.piece} ({props.rank}, {props.file})</p> */}
      <p>{props.rank}, {props.file}</p>
    </div>
  )
}

export default Square;
