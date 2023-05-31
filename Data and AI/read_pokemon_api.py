import requests, json, os

NUM_POKEMON = 1010
API_LINK = "https://pokeapi.co/api/v2/pokemon/"
OUTFILE_NAME = "pokemonapi.json"

def parse_abilities(abilities):
    result = []
    for ability in abilities:
        abil_dic = {}
        abil_dic["name"] = ability["ability"]["name"]
        abil_dic["hidden"] = ability["is_hidden"]
        abil_dic["slot"] = ability["slot"]
        result.append(abil_dic)
    return result

def parse_forms(forms):
    result = []
    for form in forms:
        result.append(form["name"])
    return result

def parse_held_items(held_items):
    result = []
    for item in held_items:
        result.append(item["item"]["name"])
    return result

def parse_past_types(past_types):
    result = []
    if len(past_types) == 0: return result
    try:
        types = past_types["types"]
    except:
        types = []
    for type in types:
        if not type["type"]["name"] in result: 
            result.append(type["type"]["name"])
    return result

def parse_stats(stats):
    result = []
    for stat in stats:
        stat_dic = {}
        stat_dic["name"] = stat["stat"]["name"]
        stat_dic["value"] = stat["base_stat"]
        stat_dic["effort"] = stat["effort"]
        result.append(stat_dic)
    return result

def parse_types(types):
    result = []
    for type in types:
        type_dic = {}
        type_dic["slot"] = type["slot"]
        type_dic["name"] = type["type"]["name"]
        result.append(type_dic)
    return result

def parse_api_entry(data):
    result = {}
    result["abilities"] = parse_abilities(data["abilities"])
    result["base_experience"] = data["base_experience"]
    result["forms"] = parse_forms(data["forms"])
    result["height"] = str(data["height"])
    result["held_items"] = parse_held_items(data["held_items"])
    result["id"] = str(data["id"])
    result["is_default"] = data["is_default"]
    result["name"] = data["name"]
    result["order"] = str(data["order"])
    result["past_types"] = parse_past_types(data["past_types"])
    result["stats"] = parse_stats(data["stats"])
    result["weight"] = str(data["weight"])
    result["types"] = parse_types(data["types"])
    return result

def read_pokemon():
    results = []
    for i in range(1, NUM_POKEMON+1):
        target = API_LINK + str(i)
        response = requests.get(target).json()
        result = parse_api_entry(response)
        results.append(result)
    return results

def write_pokemon(pokemons, outfile):
    for index, pokemon in enumerate(pokemons):
        outfile.write("\"" + pokemon["name"] + "\" : [ \n")
        outfile.write(str(pokemon) + "],\n")
        outfile.write("\n")

def main():
    outfile = open(OUTFILE_NAME, 'w')
    pokemons = read_pokemon()

    outfile.write("{ \"pokemon\" : {\n")
    write_pokemon(pokemons, outfile)
    outfile.write("}}")

main()
