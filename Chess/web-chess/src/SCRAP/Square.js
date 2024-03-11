import "./Square.css"

export default function Square (props) {
  let file = 1
  let rank = 0

  let color = "black"
  if ((file % 2 === 0 && rank % 2 === 1) || (file % 2 === 1 && rank % 2 === 0)) {
    color = "white"
  }

  return (
    <div className={color==="black" ? "blackSquare" : "whiteSquare"}>
      <p>{props.rank},{props.file}</p>
    </div>
  )
}