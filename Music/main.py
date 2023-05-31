import os, sys
from Key import Key
from Chord import Chord, ChordInKey
from CONSTANTS import NOTES_FLAT, NOTES_SHARP

def transpose_chord(old_key, new_key, old_chord):
    OLD_NOTES = old_key.notes
    idxs = []
    for note in old_chord.notes:
        idxs.append(OLD_NOTES.index(note))

    if (old_key.mood == "major" and new_key.mood == "minor"):
        for idx in idxs:
            if idx+1 in [5, 10, 12]:
                idx -= 1
    
    if (old_key.mood == "minor" and new_key.mood == "major"):
        for idx in idxs:
            if idx+1 in [4, 9, 11]:
                idx += 1

    NEW_NOTES = new_key.notes
    new_chord = []
    for idx in idxs:
        new_chord.append(NEW_NOTES[idx])
    
    res = Chord(new_chord)
    return res


def main():
    if (len(sys.argv) > 1):
        main_with_file(sys.argv[1])
    else:
        main_without_file()

def main_without_file():
    print("You're going to input the CURRENT key of the song")
    in_note = input("Note Name [A-G]: ")
    in_acc = input("Accidental [\"b\", \"#\", \"\"]: ")
    in_mood = input("Mood [\"major\", \"minor\"]: ")
    curr_key = Key(in_note, in_acc, in_mood)

    print("\nNow you're going to enter the NEW key of the song")
    in_note = input("Note Name [A-G]: ")
    in_acc = input("Accidental [\"b\", \"#\", \"\"]: ")
    in_mood = input("Mood [\"major\", \"minor\"]: ")
    new_key = Key(in_note, in_acc, in_mood)

    os.system("cls")
    print("Current Key: " + curr_key.stringify_name() + "       New Key: " + new_key.stringify_name())

    print("\n\nNow you're going to input chords in the old key. Chords are composed of 3 notes, with a space between each (ex. A C# E)")
    chords = []
    enter_chord = True
    while (enter_chord):
        in_str = input("\nEnter chord or type 'q' to quit: ")
        if (in_str == "q"):
            enter_chord = False
            break

        chord_arr = str.split(in_str, " ")
        if (len(chord_arr) != 3):
            print("ERROR: Incorrect chord formatting")
        else:
            new_chord = Chord(chord_arr)
            chords.append(new_chord)

    transposed_chords = []
    for chord in chords:
        transposed_chords.append(transpose_chord(curr_key, new_key, chord))

    print("Original Chords:")
    for chord in chords:
        chord.print_name()
    
    print("Transposed Chords:")
    for chord in transposed_chords:
        chord.print_name()

"""
This is just for testing. 
1. Copy the current contents of main
2. Remove instructional print statements (optional)
3. Replace any input() with file.readline()
"""
def main_with_file(infile):
    inputs = [line.rstrip() for line in open(infile, 'r')]

    in_note = inputs.pop(0)
    in_acc = inputs.pop(0)
    in_mood = inputs.pop(0)
    curr_key = Key(in_note, in_acc, in_mood)

    in_note = inputs.pop(0)
    in_acc = inputs.pop(0)
    in_mood = inputs.pop(0)
    new_key = Key(in_note, in_acc, in_mood)

    print("Current Key: " + curr_key.stringify_name() + "       New Key: " + new_key.stringify_name() + "\n")

    chords = []
    enter_chord = True
    while (enter_chord):
        in_str = inputs.pop(0)
        if (in_str == "q"):
            enter_chord = False
            break

        chord_arr = str.split(in_str, " ")
        if (len(chord_arr) != 3):
            print("ERROR: Incorrect chord formatting")
        else:
            new_chord = Chord(chord_arr)
            chords.append(new_chord)

    transposed_chords = []
    for chord in chords:
        transposed_chords.append(transpose_chord(curr_key, new_key, chord))

    print("Original Chords:")
    for chord in chords:
        chord.print_name()
    
    print("Transposed Chords:")
    for chord in transposed_chords:
        chord.print_name()

if __name__ == "__main__":
    main()