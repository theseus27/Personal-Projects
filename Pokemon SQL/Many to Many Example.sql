CREATE DATABASE IF NOT EXISTS TEST;
USE TEST;
CREATE TABLE IF NOT EXISTS MAIN(PokemonNum int NOT NULL, PokemonName varchar(30), PRIMARY KEY (PokemonName));
CREATE TABLE IF NOT EXISTS TYPJOIN(PokemonNum int NOT NULL, Typ varchar(20));
CREATE TABLE IF NOT EXISTS TYPS(Typ varchar(20));
CREATE TABLE IF NOT EXISTS ABILITYJOIN(PokemonNum int NOT NULL, Ability varchar(30));
CREATE TABLE IF NOT EXISTS ABILITIES(Ability varchar(30), Descrip varchar(1000));

INSERT INTO MAIN(PokedexNumber, PokemonName) VALUES(1, "Bulbasaur");
INSERT INTO TPJOIN(PokedexNumber, Tp) VALUES(1, "Grass");
INSERT INTO TPJOIN(PokedexNumber, Tp) VALUES(1, "Poison");
INSERT INTO TPS(Tp) VALUES("Grass");
INSERT INTO TPS(Tp) VALUES("Poison");
INSERT INTO ABILITYJOIN(PokedexNumber, Ability) VALUES(1, "Overgrow");
INSERT INTO ABILITYJOIN(PokedexNumber, Ability) VALUES(1, "Chlorophyll");
INSERT INTO ABILITIES(Ability, Descrip) VALUES("Overgrow", "Strengthens grass moves to inflict 1.5× damage at 1/3 max HP or less.");
INSERT INTO ABILITIES(Ability, Descrip) VALUES("Chlorophyll", "Doubles Speed during strong sunlight.");

