import React from "react"

const Pokemon = ({ pokemon, showPokemonInfo}) => {
  return (
    pokemon && (
      <>
        <div
          onClick = {(e) => {showPokemonInfo(); e.stopPropagation()}}
          className = "flex flex-wrap"
        >
          <div ClassName="w-full">
            <div className = "relative flex flex-col">
              <h2 className = "title-font">
                {pokemon?.pokemonName}
              </h2>
            </div>
          </div>
        </div>
      </>
    )
  )
}

export default Pokemon