import Pokemon from "../Pokemon";
import React, {useState} from "react";
import PopupModal from "../Modal/PopupModal";

const PokemonTable = ({pokemonSet}) => {
  const [pokemonInfo, setPokemonInfo] = useState(false)

  return (
    <>
      <div className="sections-list">
        {pokemonSet.length && (
          pokemonSet.map((pokemon) => (
            <Pokemon showPokemonInfo={() => setPokemonInfo(pokemon)}
            key = {pokemon.id} pokemon = {pokemon} />
          ))
        )}
        {!pokemonSet.length && (
          <p>No Pokemon found :/</p>
        )}
      </div>
      {pokemonInfo && <PopupModal
        modalTitle = {"Pokemon Info"}
        onCloseBtnPress = {() => {
          setPokemonInfo(false);
        }}  
      >
      </PopupModal>}
    </>
  )
}

export default PokemonTable