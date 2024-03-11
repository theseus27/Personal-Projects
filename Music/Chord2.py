import Key as K
from Key import Key as Key
from collections import defaultdict
from CONSTANTS import NOTES_FLAT, NOTES_SHARP

class Chord:
    def __init__(self, notes, relative_key, main_note, inversion):
        self.notes = notes
        self.relative_key = relative_key
        self.main_note = main_note
        self.inversion = inversion

    def printchord(self):
        print(self.main_note, end=" ")
        print("(inv " + str(self.inversion) + ")", end=" ")
        print("in the key of " + self.relative_key + ":  ", end=" ")
        print(self.notes)

NUMNOTES = 12
NUMKEYS = 14
KEYS = []
CHORDS = []

# Creates the 14 major keys
def generate_major_keys():
    keynames = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb", "G", "D", "A", "E", "B", "F#", "C#"]
    
    for keyname in keynames: 
        KEYS.append(Key(keyname, "major"))

# There are 24 unique chords
def generate_unique_chords():
    generate_major_keys()

    unique_chords = []
    NOTE_COMBOS = defaultdict(int)

    for k in KEYS:
        main_notes = k.notes
        key_notes = k.get_main_note_idxs()
        for idx in range(7):
            key_note = key_notes[idx] - 1
            notes = []
            notes.append(main_notes[key_note])
            notes.append(main_notes[(key_note + 4) % 12])
            notes.append(main_notes[(key_note + 8) % 12])

            notestr = notes[0] + " " + notes[1] + " " + notes[2]
            NOTE_COMBOS[notestr] += 1
    
    for combo in NOTE_COMBOS.keys():
        print(combo + ": " + str(NOTE_COMBOS[combo]))

# For every key, figure out what the 7 'main' notes are
# For each of those 7 main notes, find the 1/3/5 within that key
# Save the chord as it's zero, first, second inversions
    # There are 14 keys * 7 notes * 3 inversions = 294 chords
def generate_chords():
    generate_major_keys()

    for k in KEYS:
        main_notes = k.notes_start_c()
        key_notes = k.get_main_note_idxs()
        for idx in range(7):
            key_note = key_notes[idx] - 1
            notes = []

            notes.append(main_notes[key_note])
            notes.append(main_notes[(key_note + 4) % 12])
            notes.append(main_notes[(key_note + 7) % 12])
            inv1 = [notes[1], notes[2], notes[0]]
            inv2 = [notes[2], notes[0], notes[1]]
            CHORDS.append(Chord(notes, k.name, notes[0], 0))
            CHORDS.append(Chord(inv1, k.name, notes[0], 1))
            CHORDS.append(Chord(inv2, k.name, notes[0], 2))

# There are 36 unique chords with inversions
def unique_with_inversions():
    generate_chords()
    unique_chords = []
    unique_chord_set = set()
    for chord in CHORDS:
        chord_str = ""
        if chord.notes[0] in NOTES_SHARP:
            chord_str += str(NOTES_SHARP.index(chord.notes[0]))
            chord_str += ", "
        else:
            chord_str += str(NOTES_FLAT.index(chord.notes[0]))
            chord_str += ", "

        if chord.notes[1] in NOTES_SHARP:
            chord_str += str(NOTES_SHARP.index(chord.notes[1]))
            chord_str += ", "
        else:
            chord_str += str(NOTES_FLAT.index(chord.notes[1]))
            chord_str += ", "

        if chord.notes[2] in NOTES_SHARP:
            chord_str += str(NOTES_SHARP.index(chord.notes[2]))
            chord_str += ", "
        else:
            chord_str += str(NOTES_FLAT.index(chord.notes[2]))
            chord_str += ", "

        if chord_str not in unique_chord_set:
            unique_chord_set.add(chord_str)
            unique_chords.append(chord)
    return unique_chords

# For each inversion, count how many times each pattern occurs
def sort_patterns(inversion):
    counter = {"WWW":0, "BBB":0, "WBW":0, "BWB":0, "WWB":0, "BWW":0, "BBW":0, "WBB":0}
    for chord in CHORDS:
        if chord.inversion != inversion:
            continue
        patstr = ""
        for note in chord.notes:
            if len(note) > 1:
                patstr += "B"
            else:
                patstr += "W"
        counter[patstr] += 1
    
    for k in counter.keys():
        print(k + ": " + str(counter[k]))


CHORDS = unique_with_inversions()
print("Inversion 0")
sort_patterns(0)
print("\n\nInversion 1")
sort_patterns(1)
print("\n\nInversion 2")
sort_patterns(2)







def test_key(name):
    AKEY = Key(name, "major")
    main_notes = AKEY.notes_start_c()
    key_notes = AKEY.get_main_note_idxs()
    print(main_notes)
    print(key_notes)

    for idx in range(7):
        key_note = key_notes[idx] - 1
        notes = []

        notes.append(main_notes[key_note])
        notes.append(main_notes[(key_note + 4) % 12])
        notes.append(main_notes[(key_note + 7) % 12])
        inv1 = [notes[1], notes[2], notes[0]]
        inv2 = [notes[2], notes[0], notes[1]]
        print(notes)
        print(inv1)
        print(inv2)
        print("\n")
# test_key("A")
# test_key("F")