import commands as comm
import setup as setup
POKEMON_EXISTING = 905
ABILITIES_EXISTING = 267
MOVES_EXISTING = 826

def main():
    connection = comm.connect("pokemondb")
    
    #SETUP DB and TABLES
    connection = setup.initialize(connection)
        
    #Populate Pokemon
    setup.pokemon(connection, POKEMON_EXISTING)
    
    setup.abilities(connection, ABILITIES_EXISTING)
    
    setup.moves(connection, MOVES_EXISTING)
    
if (__name__ == "__main__"):
    main()
