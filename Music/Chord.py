from Key import Key
from CONSTANTS import NOTES_FLAT, NOTES_SHARP

class Chord:
    def __init__(self, notes):
        self.notes = []
        self.inversion = 0
        self.key_name = ""
        self.mood = "major"

        if notes == []:
            return
        
        if (len(notes) != 3):
            print("ERROR: Currently only supports 3-note chords")
            return

        hasFlat = False
        hasSharp = False

        for note in notes:
            self.notes.append(str.capitalize(note))

        for note in self.notes:
            if "#" in note: hasSharp = True
            if "b" in note: hasFlat = True

        if (hasFlat and hasSharp):
            print("ERROR: Chords can't contain sharps and flats")
            return
    
        NOTE_LIST = NOTES_SHARP
        if (hasFlat):
            NOTE_LIST = NOTES_FLAT
        
        idxs = []
        for note in self.notes:
            if note not in NOTE_LIST:
                print("ERROR: Note not found in note list")
                return
            idxs.append(NOTE_LIST.index(note))

        diff1 = (idxs[1] - idxs[0]) % 12
        diff2 = (idxs[2] - idxs[1]) % 12

        # Major Normal
        if (diff1 == 4 and diff2 == 3):
            self.key_name = self.notes[0]
        
        # Major 1st Inversion
        elif (diff1 == 3 and diff2 == 5):
            self.inversion = 1
            self.key_name = self.notes[2]

        # Major 2nd Inversion
        elif (diff1 == 5 and diff2 == 4):
            self.inversion = 2
            self.key_name = self.notes[1]

        # Minor Normal
        elif (diff1 == 3 and diff2 == 4):
            self.mood = "minor"
            self.key_name = self.notes[0]

        # Minor 1st Inversion
        elif (diff1 == 4 and diff2 == 5):
            self.mood = "minor"
            self.inversion = 1
            self.key_name = self.notes[2]
        
        elif (diff1 == 5 and diff2 == 3):
            self.mood = "minor"
            self.inversion = 2
            self.key_name = self.notes[1]

        else:
            print("ERROR: Chord could not be recognized")
            print("Input: " + str(self.notes))

    def print_name(self):

        if (self.notes == [] or self.key_name == ""):
            print("This is not a complete chord.")
            return

        print(str(self.notes) + " => " + self.key_name, end="")

        if (self.mood == "minor"):
            print("m", end="")

        if (self.inversion == 0):
            print("")
        elif (self.inversion == 1):
            print(" inv. 1")
        elif (self.inversion == 2):
            print(" inv. 2")



class ChordInKey(Chord):
    rel_key = None
    position = 1
    note_idxs = []
    name = ""

    def __init__(self, super_obj, rel_key):
        self.rel_key = rel_key
        if (self.note_idxs == [] and self.notes == []):
            print("ERROR: ChordInKey needs note idxs or a super_obj with note names")
            return
        

