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
