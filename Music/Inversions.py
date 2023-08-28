from Key import Key
from Chord import Chord

# Chords: list of chords (ex. if key=D then a chord of 1 is D)
# In general, first to second should go down, second to third should go up, third to fourth should go down
def get_inversions(chords, key):
    key_notes = key.notes

    inversions = []

    for chord in chords:
        chord_notes = chord.notes

        distance_0 = max(key_notes.index(chord_notes[0])), (0 - key_notes.index(chord_notes[0]) % 7)
        distance_1 = max(key_notes.index(chord_notes[1])), (0 - key_notes.index(chord_notes[1]) % 7)
        distance_2 = max(key_notes.index(chord_notes[2])), (0 - key_notes.index(chord_notes[2]) % 7)

        if distance_0 <= distance_1 and distance_0 <= distance_2:
            inversions.append(0)
        elif distance_1 <= distance_2:
            inversions.append(1)
        else:
            inversions.append(2)
    
    for i in len(chords):
        chord_notes = chords[i].notes
        chord_name = key_notes[chord_notes[0] - 1]
        inversion_order = ""
        if inversions[i] == 0:
            inversion_order = str(chord_notes[0]) + " " + str(chord_notes[1]) + " " + str(chord_notes[2])
        elif inversions[i] == 1:
            inversion_order = str(chord_notes[1]) + " " + str(chord_notes[2]) + " " + str(chord_notes[0])
        else:
            inversion_order = str(chord_notes[2]) + " " + str(chord_notes[0]) + " " + str(chord_notes[1])

        print(chord_name + " (inversion " + str(inversions[i]) + " ): " + inversion_order)

# Testing
key = Key("D", None, None)
chords = [Chord(["D", "F#", "A"]), Chord(["G", "B", "D"]), Chord(["E", "G", "B"]), Chord(["A", "C", "E"])]
get_inversions(chords, key)
