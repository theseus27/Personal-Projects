from constants import NUM_NOTES, NUMERIC, LETTERS, MAJOR_INTERVALS, MINOR_INTERVALS

KEY = "C"
MAJOR = True
SHARPS = True
SCALE = ["C", "D", "E", "F", "G", "A", "B"]

def set_key():
    global KEY, MAJOR

    valid_key = False
    while not valid_key:
        new_key = str.capitalize(input("Enter the key you want to be in: "))
        if (new_key not in NUMERIC.keys()):
            print("Invalid input")
        else:
            KEY = new_key
            valid_key = True

    valid_major_minor = False
    while not valid_major_minor:
        mm = str.capitalize(input("\'Major\' or \'Minor\': "))
        if (mm == "Major"):
            MAJOR = True
            valid_major_minor = True
        elif (mm == "Minor"):
            MAJOR = False
            valid_major_minor = True
        
        set_sharps()
        set_scale()

def set_scale():
    global SCALE

    if MAJOR:
        nums = MAJOR_INTERVALS.copy()
    else:
        nums = MINOR_INTERVALS.copy()

    diff = NUMERIC[KEY] - 1
    shifted = [(((diff + nums[i])) % 12) for i in range(7)]
    shifted = [12 if shifted[i] == 0 else shifted[i] for i in range(7)]

    print(shifted)

    new_scale = []

    for i in range(7):
        note = shifted[i]
        if LETTERS[note]["normal"] != "none":
            new_scale.append(LETTERS[note]["normal"])

        elif SHARPS:
            if LETTERS[note]["sharp"] != "none":
                new_scale.append(LETTERS[note]["sharp"])
            else:
                new_scale.append(LETTERS[note]["flat"])

        else:
            if LETTERS[note]["flat"] != "none":
                new_scale.append(LETTERS[note]["flat"])
            else:
                new_scale.append(LETTERS[note]["sharp"])

        SCALE = new_scale
 
def set_sharps():
    global SHARPS

    if len(KEY) == 1:
        # C, D, E, G, A, B major
        if (MAJOR == True and KEY != "F"):
            SHARPS = True
        # F major
        elif (MAJOR == True):
            SHARPS = False
        # E, B minor
        if (MAJOR == False and (KEY == "B" or KEY == "E")):
            SHARPS = True
        # C, D, F, G, A minor
        elif (MAJOR == False):
            SHARPS = False
        else:
            print("set_sharps() error 1")
    
    elif (KEY[1] == '#'):
        SHARPS = True
    
    elif (KEY[1] == 'b'):
        SHARPS = False
    else:
        print("set_sharps() error 2")

def chord_per_key():
    print("Primary Chords:")
    for i in [1, 4, 5]:
        NOTE = NUMERIC[SCALE[i]]
        third = NOTE+2
        print(SCALE[i], " : ", SCALE[i], )
    for i in [2, 3, 6, 7]:


def main():
    set_key()
    if (MAJOR):
        print("The key is now " + KEY + " Major.")
    else:
        print("The key is now " + KEY + " Minor.")
    
    print("Scale: ", SCALE)

main()


NUM_NOTES = 12
NUMERIC = {"C" : 1, "C#" : 2, "Db" : 2, "D" : 3, "D#" : 4, "Eb" : 4, "E" : 5, "E#" : 6, "Fb" : 5, "F" : 6, "F#" : 7, "Gb" : 7, "G" : 8, "G#" : 9, "Ab" : 9, "A" : 10, "A#" : 11, "Bb" : 11, "B" : 12, "B#" : 1, "Cb" : 12}

note_dic1 = {"normal"  : "C", "sharp" : "B#",  "flat" : "none"}
note_dic2 = {"normal"  : "none", "sharp" : "C#",  "flat" : "Db"}
note_dic3 = {"normal"  : "D", "sharp" : "none",  "flat" : "none"}
note_dic4 = {"normal"  : "none", "sharp" : "D#",  "flat" : "Eb"}
note_dic5 = {"normal"  : "E", "sharp" : "none",  "flat" : "Fb"}
note_dic6 = {"normal"  : "F", "sharp" : "E#",  "flat" : "none"}
note_dic7 = {"normal"  : "none", "sharp" : "F#",  "flat" : "Gb"}
note_dic8 = {"normal"  : "G", "sharp" : "none",  "flat" : "none"}
note_dic9 = {"normal"  : "none", "sharp" : "G#",  "flat" : "Ab"}
note_dic10 = {"normal"  : "A", "sharp" : "none",  "flat" : "none"}
note_dic11 = {"normal"  : "none", "sharp" : "A#",  "flat" : "Bb"}
note_dic12 = {"normal"  : "B", "sharp" : "none",  "flat" : "Cb"}
LETTERS = {}
LETTERS[0] = None
LETTERS[1] = note_dic1
LETTERS[2] = note_dic2
LETTERS[3] = note_dic3
LETTERS[4] = note_dic4
LETTERS[5] = note_dic5
LETTERS[6] = note_dic6
LETTERS[7] = note_dic7
LETTERS[8] = note_dic8
LETTERS[9] = note_dic9
LETTERS[10] = note_dic10
LETTERS[11] = note_dic11
LETTERS[12] = note_dic12

MAJOR_INTERVALS = [1, 3, 5, 6, 8, 10, 12]
MINOR_INTERVALS = [1, 3, 4, 6, 8, 9, 11]