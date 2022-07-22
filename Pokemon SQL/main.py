import commands as commands
import createDB as create
POKEMON_EXISTING = 905

def main():
    #Populate Pokedex Table
    connection = commands.connect("")
    connection = create.initialize(connection)
    create.populate(connection, POKEMON_EXISTING)

if (__name__ == "__main__"):
    main()
