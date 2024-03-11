import "./Board.css"
import Square from "./Square"

export default function Board () {
  const rows = 8;
  const cols = 8;
  
  const generateBoard = () => {
    const board = [];
    for (let row = 0; row < rows; row++) {
      const mini = [];
      for (let col = 0; col < cols; col++) {
        mini.push(
          <div className="grid-item">
            <Square key={`${row}-${col}`} rank={row} file={col}/>
          </div>);
      }
      board.push(mini);
    }
    return (board);
  };
  
  return (generateBoard());


  // let squares = Array(64).fill("x")

  // return (
  //   <>
  //   <div className="board">

  //     {squares.map((piece, i) => (
  //       <Square piece={piece} num={i}/>
  //       // <div className="whiteSquare">
  //       //   <p>{piece}</p>
  //       // </div>
  //     ))}

  //   </div>
  //   </>
  // )
} 