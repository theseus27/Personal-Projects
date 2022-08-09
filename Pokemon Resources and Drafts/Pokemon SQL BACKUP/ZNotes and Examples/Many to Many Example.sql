DROP DATABASE IF EXISTS TEST;
CREATE DATABASE IF NOT EXISTS TEST;
USE TEST;

CREATE TABLE IF NOT EXISTS Pokemon(ID int NOT NULL PRIMARY KEY, name varchar(30) NOT NULL);
CREATE TABLE IF NOT EXISTS Type(ID int NOT NULL PRIMARY KEY, type varchar(20) NOT NULL);
CREATE TABLE IF NOT EXISTS BaseStats(ID int NOT NULL PRIMARY KEY, att int NOT NULL, def int NOT NULL, hp int NOT NULL, spAtt int NOT NULL, spDef int NOT NULL, speed int NOT NULL);
CREATE TABLE IF NOT EXISTS Abilities(ID int NOT NULL PRIMARY KEY, ability varchar(30) NOT NULL, Descrip varchar(1000));

CREATE TABLE IF NOT EXISTS Pokemon_Typ(PT_RelationID INT AUTO_INCREMENT PRIMARY KEY, PokemonID int NOT NULL, TypID int NOT NULL, FOREIGN KEY(PokemonID) REFERENCES POKEMON(PokemonID), FOREIGN KEY(TypID) REFERENCES Typ(TypID));
CREATE TABLE IF NOT EXISTS Pokemon_Ability(PA_RelationID INT AUTO_INCREMENT PRIMARY KEY, PokemonID int NOT NULL, AbilityID int NOT NULL, FOREIGN KEY(PokemonID) REFERENCES POKEMON(PokemonID), FOREIGN KEY(AbilityID) REFERENCES Ability(AbilityID));

INSERT INTO Pokemon(PokemonID, PokemonName) VALUES(1, "Bulbasaur");
INSERT INTO Typ(TypID, Typ) VALUES(1, "Grass");
INSERT INTO Typ(TypID, Typ) VALUES(2, "Poison");
INSERT INTO Ability(AbilityID, Ability, Descrip) VALUES(1, "Overgrow", "Strengthens grass moves to inflict 1.5× damage at 1/3 max HP or less.");
INSERT INTO Ability(AbilityID, Ability, Descrip) VALUES(2, "Chlorophyll", "Doubles Speed during strong sunlight.");
INSERT INTO Pokemon_Typ(PokemonID, TypID) VALUES (1, 1);
INSERT INTO Pokemon_Typ(PokemonID, TypID) VALUES (1, 2);

SELECT Pokemon.PokemonName, Typ.Typ, PT_RelationID FROM Pokemon_Typ
INNER JOIN Pokemon ON Pokemon_Typ.PokemonID = Pokemon.PokemonID
INNER JOIN Typ ON Pokemon_Typ.TypID = Typ.TypID;
