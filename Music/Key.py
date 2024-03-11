from CONSTANTS import NOTES_FLAT, NOTES_SHARP, MAJOR_MAIN_IDX, MINOR_MAIN_IDX

def index_note(notes, note, accidental):
    if (accidental != ""):
        note += accidental
    try:
        idx = notes.index(note)
    except:
        print("ERROR: Note not find in this key's notes")
    return idx

class Key:
    def __init__ (self, name, mood):
        self.mood = mood
        self.notes = []
        self.main_notes = []
        self.name = name
        self.note = ""
        error = False

        raw_note = ""
        raw_acc = ""
        if len(name) > 1:
            raw_note = str.capitalize(name[0])
            raw_acc = name[1]
        else:
            raw_note = str.capitalize(name[0])

        if raw_note in ["C", "D", "E", "F", "G", "A", "B"]:
            self.note = raw_note
        else:
            error = True

        if raw_acc in ["", "b", "#"]:
            self.accidental = raw_acc
        else:
            error = True

        if error:
            print("WARNING: One or more fields is invalid. Your current key is: " + self.stringify_name() + "\n")

        key_changed = self.validate_key()
        if key_changed:
            print("WARNING: The key you entered is theoretical and has been adjusted. Your new key is: " + self.stringify_name() + "\n")

        self.set_notes()
        self.main_notes = self.get_main_notes()

    # def __init__(self, note, accidental, mood):
    #     self.note = note
    #     self.accidental = accidental
    #     self.mood = mood
    #     self.notes = []
    #     error = False

    #     if str.capitalize(note) in ["C", "D", "E", "F", "G", "A", "B"]:
    #         self.note = str.capitalize(note)
    #     else:
    #         error = True

    #     if accidental in ["", "b", "#"]:
    #         self.accidental = accidental
    #     else:
    #         error = True

    #     if str.lower(mood) in ["major", "minor"]:
    #         self.mood = str.lower(mood)
    #     else:
    #         error = True

    #     if error:
    #         print("WARNING: One or more fields is invalid. Your current key is: " + self.stringify_name() + "\n")

    #     key_changed = self.validate_key()
    #     if key_changed:
    #         print("WARNING: The key you entered is theoretical and has been adjusted. Your new key is: " + self.stringify_name() + "\n")

    #     self.set_notes()

    def stringify_name(self):
        result = self.note
        if self.accidental != "":
            result += self.accidental
        result += " "
        result += self.mood
        return result

    def validate_key(self):
        change = False

        if (self.mood == "major"):
            if (self.accidental == "b"):
                if (self.note == "F"):
                    self.note = "E"
                    self.accidental = ""
                    change = True
            elif (self.accidental == "#"):
                if (self.note == "D"):
                    self.note = "E"
                    self.accidental = "b"
                    change = True
                elif (self.note == "E"):
                    self.note = "F"
                    self.accidental = ""
                    change = True
                elif (self.note == "G"):
                    self.note = "A"
                    self.accidental = "b"
                    change = True
                elif (self.note == "A"):
                    self.note = "B"
                    self.accidental = "b"
                    change = True
                elif (self.note == "B"):
                    self.note = "C"
                    self.accidental = ""
                    change = True
        
        elif (self.mood == "minor"):
            if (self.accidental == "b"):
                if (self.note == "C"):
                    self.note = "B"
                    self.accidental = ""
                    change = True
                elif (self.note == "D"):
                    self.note = "C"
                    self.accidental = ""
                    change = True
                elif (self.note == "F"):
                    self.note = "E"
                    self.accidental = ""
                    change = True
                elif (self.note == "G"):
                    self.note = "F"
                    self.accidental = "#"
                    change = True
            elif (self.accidental == "#"):
                if (self.note == "E"):
                    self.note = "F"
                    self.accidental = ""
                    change = True
                elif (self.note == "B"):
                    self.note = "C"
                    self.accidental = ""
                    change = True
        return change

    def set_notes(self):
        notes_copy = NOTES_SHARP

        if (self.accidental == "b"):
            notes_copy = NOTES_FLAT
        elif (self.accidental == ""):
            if (self.mood == "major" and self.note == "F"):
                notes_copy = NOTES_FLAT
            elif (self.mood == "minor" and self.note in ["C", "D", "F", "G", "A"]):
                notes_copy = NOTES_FLAT

        starting_index = index_note(notes_copy, self.note, self.accidental)
        new_notes = []
        for i in range(12):
            new_notes.append(notes_copy[(i+starting_index) % 12])
        self.notes = new_notes

    def get_main_notes(self):
        res = []
        if (self.mood == "major"):
            for i in range(7):
                res.append(self.notes[MAJOR_MAIN_IDX[i] - 1])
        else:
            for i in range(7):
                res.append(self.notes[MINOR_MAIN_IDX[i] - 1])
        return res
    
    def print_stats(self):
        print(f'{"Current Key: ":15}' + self.stringify_name())
        print(f'{"All Notes: ":15}' + str(self.notes))
        print(f'{"Main Notes: ":15}' + str(self.main_notes()))

    def get_main_note_idxs(self):
        sharp_notes = NOTES_SHARP
        flat_notes = NOTES_FLAT
        
        note_idxs = []
        for note in self.main_notes:
            if note in sharp_notes:
                note_idxs.append(sharp_notes.index(note)+1)
            else:
                note_idxs.append(flat_notes.index(note)+1)           
        return note_idxs
    
    def notes_start_c(self):
        notes_copy = NOTES_SHARP
        if (self.accidental == "b"):
            notes_copy = NOTES_FLAT
        elif (self.accidental == ""):
            if (self.mood == "major" and self.note == "F"):
                notes_copy = NOTES_FLAT  
        return notes_copy 

    def chord_idx_to_notes(self, chord):
        notes_copy = NOTES_SHARP
        if (self.accidental == "b"):
            notes_copy = NOTES_FLAT
        elif (self.accidental == ""):
            if (self.mood == "major" and self.note == "F"):
                notes_copy = NOTES_FLAT

        notes = []
        for x in chord:
            notes.append(notes_copy[x-1])
        return notes