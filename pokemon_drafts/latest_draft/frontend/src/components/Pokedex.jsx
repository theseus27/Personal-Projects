import React, { useEffect, useState, Component } from "react";

//useState hook manages application's local state
//useEffect hook allows operations such as data fetching

const PokemonContext = React.createContext({
  allPokemon: [], fetchPokemon: () => {}
})

export default function Pokedex() {
  const [allPokemon, setPokemon] = useState([])

  const fetchPokemon = async () => {
    const response = await fetch("http://127.0.0.1:8000/pokemon");
    console.log(response)
    const allPokemon = await response.json();
    setPokemon(allPokemon.data);
  }

  useEffect(() => {
    fetchPokemon()
  }, [])

  return (
    <>
      <h1>Pokedex</h1>
        <PokemonContext.Provider value= {{allPokemon, fetchPokemon}}>
        <div className="pokemon-grid">
          {allPokemon.map((pokemon) => (
            <b>{pokemon.num} {pokemon.name} <img src={pokemon.img} alt="{pokemon.name}"/></b>
          ))}
        </div>
      </PokemonContext.Provider>
    </>
  )
}
