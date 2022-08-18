import React, { useEffect, useState, Component } from "react";
import { Box, Button, Flex, Input, InputGroup, Modal, ModalBody, ModalCloseButton, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Stack, Text, useDisclosure } from "@chakra-ui/react"

//useState hook manages application's local state
//useEffect hook allows operations such as data fetching

const PokemonContext = React.createContext({
  allPokemon: [], fetchPokemon: () => {}
})

export default function Pokedex() {
  const [allPokemon, setPokemon] = useState([])

  const fetchPokemon = async () => {
    const response = await fetch("http://localhost:8000/pokemon");
    const allPokemon = await response.json();
    setPokemon(allPokemon.data);
  }

  useEffect(() => {
    fetchPokemon()
  }, [])

  return (
    <PokemonContext.Provider value= {{allPokemon, fetchPokemon}}>
      <AddPokemon />
      <Stack spacing= {5}>
        {allPokemon.map((pokemon) => (
          <b>{pokemon.num} {pokemon.name} <img src={pokemon.img} alt="{pokemon.name}"/></b>
        ))}
      </Stack>
    </PokemonContext.Provider>
  )
}


function AddPokemon() {
  const [num, name, img, setPokemon] = React.useState("");
  const {allPokemon, fetchPokemon} = React.useContext(PokemonContext);

  const handleInput = event => {
    setPokemon(event.target.value);
  }
  
  const handleSubmit = (event) => {
    const newPokemon = {
      "id": allPokemon.length + 1,
      "num": num,
      "name": name,
      "img": img,
    };
  
    fetch("http://localhost:8000/pokemon", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newPokemon) 
    }).then(fetchPokemon);
  }

  return (
    <form onSubmit={handleSubmit}>
      <InputGroup size="md">
        <Input
          pr = "4.5rem"
          type = "text"
          placeholder = "Add a Pokemon"
          aria-label = "Add a Pokemon"
          onChange = {handleInput}
        />
      </InputGroup>
    </form>
  )
}

