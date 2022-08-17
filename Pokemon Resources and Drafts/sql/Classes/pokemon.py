from typing import List

class PokemonTemplate():
    def __init__(self, name:str, id:int, types:List, exp:int, bSt:List):
        self.name = name
        self.dexNum = id
        self.types = types
        self.baseEXP = exp
        self.baseStats = [
            {"att": "HP", "value":{"stat": bSt[0][0], "effort":bSt[0][1]}},
            {"att": "Att", "value":{"stat": bSt[1][0], "effort":bSt[1][1]}},
            {"att": "Def", "value":{"stat": bSt[2][0], "effort":bSt[2][1]}},
            {"att": "SpAtt", "value":{"stat": bSt[3][0], "effort":bSt[3][1]}},
            {"att": "SpDef", "value":{"stat": bSt[4][0], "effort":bSt[4][1]}},
            {"att": "Sp", "value":{"stat": bSt[5][0], "effort":bSt[5][1]}}
        ]
        
    def printStats(self):
        print("Name: " + str(self.name))
        print("Pokedex Number: " + str(self.dexNum))
        print("Type(s): " + str(self.types))
        print("Base EXP: " + str(self.baseEXP))
        print("Base Stats: ")
        for i in range(0, 6):
            print(str(self.baseStats[i].get("att")) + 
                  ": " + 
                  str(self.baseStats[i].get("value")))
        print("\n")
        
    def allData(self):
        return([self.name, self.dexNum, self.types, self.baseEXP, self.baseStats])