import config from "./config"
const axios = require("axios")

class FastAPIClient {
  constructor(overrides) {
    this.config = {
      ...config,
      ...overrides,
    };
    this.authToken = config.authToken;

    this.apiClient = this.getApiClient(this.config);
  }

  getPokemonByID(pokemonId) {
    return this.apiClient.get(`/pokemon/${pokemonId}`);
  }

  getPokemonByName(pokemonName) {
    return this.apiClient.get(`/pokemon/${pokemonName}`);
  }

  getAllPokemon() {
    return this.apiClient.get(`/pokemon`).then(({data}) => {
      return data;
    });
  }

}

export default FastAPIClient