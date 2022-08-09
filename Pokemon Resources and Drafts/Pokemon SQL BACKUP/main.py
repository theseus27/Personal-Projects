import commands as comm
import createDB as create
POKEMON_EXISTING = 905

def main():
    #Populate Pokedex Table
    connection = comm.connect("")
    connection = create.initialize(connection)
    create.populate(connection, POKEMON_EXISTING)
    #Assume Table is Populated
    connection = comm.connect("pokemondb");
    #Create.loadAbilities
    #Create.loadMoves
    
if (__name__ == "__main__"):
    main()
