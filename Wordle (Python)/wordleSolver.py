#Import packages
import os
import itertools
import numpy
from nltk.corpus import words as dictionaryList
from pip import List

#Global Consts
WORD_LENGTH = 5
GUESS_COUNT = 6
SCREEN_WIDTH = os.get_terminal_size().columns

#Build word list
DICTIONARY = set()
for word in dictionaryList.words():
    if (len(word) == WORD_LENGTH):
        DICTIONARY.add(word)

#Track what letters are possible
possibleLetters = []
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
for i in range(0, WORD_LENGTH):
    possibleLetters.append(alphabet)
print(len(possibleLetters))

#Solution
lettersInSolution = []
possibleSolutions = []

#Find words
def recurse(range, curr, end, word):
    print("Entering Recurse. Word is currently " + word + "Curr is " + str(curr))
    if (curr < end):
        for i in range:
            if i in possibleLetters[curr]:
                word += i
                recurse(range, curr+1, end, word)
    else:
        if (len(word) != WORD_LENGTH):
            print(word)
            exit("(recurse) Error: Invalid length word")
        if word in DICTIONARY:
            print(word)

#Find possible Solutions
def solve(guess: str) -> bool:
    guess = list(guess)
    if (len(guess) != WORD_LENGTH):
        exit("(solve) Error: Failed to parse word.")

    #Try All Words
    for i in alphabet:
        recurse(alphabet, 0, WORD_LENGTH, "")
        
        
    print("Possible Solutions: " + str(len(possibleSolutions)) + "\n")
    
    #Check Results
    if (len(possibleSolutions) == 1 or len(possibleSolutions) == 0):
        return True 
    else:  
        return False

def updatePossibleLetters(letter: str, index: int, value: int):
    letterIndex = ord(letter) - 93
    if (value == 0):
        for place in range(0, WORD_LENGTH):
            possibleLetters[place][letterIndex] = ""
    elif (value == 1):
        possibleLetters[index][letterIndex] = ""
        lettersInSolution.append(letter)
    elif (value == 2):
        for ind, val in enumerate(possibleLetters[index]):
            if val != letter:
                possibleLetters[index][ind] = ""
        lettersInSolution.remove(letter)
    
    if(len(lettersInSolution) == WORD_LENGTH):
        print("You have all the letters.")
    elif (len(lettersInSolution) > WORD_LENGTH):
        exit("(updatePL) Error: Too many possible letters.")

def feedback(guess: str) -> bool:
    guessList = list(guess)
    print("Type 2 for green (right letter, right place")
    print("Type 1 for yellow (right letter, wrong place")
    print("Type 0 for grey (wrong letter)\n")
    for index, letter in enumerate(guessList):
        validFeedback = False
        while (validFeedback == False):
            value = input("Feedback for " + letter + ": ")
            if (value == "0" or value == "1" or value == "2"):
                validFeedback = True
            else:
                print("Invalid Feedback: " + value)
        updatePossibleLetters(letter, index, value)
    
    hint = input("Would you like to see how many possible words are left? ")
    if ((hint.lower() == "yes") or hint.lower() == "y"):
        return solve(guess)
    else:
        return False

#Play a game
def play():
    print("\n\n\n\n", ("Welcome to Wordle Solver!\n").center(SCREEN_WIDTH))
    
    attempts = 0
    solved = False
    
    while ((attempts < GUESS_COUNT) and (solved == False)):
        validAttempt = False
        while(validAttempt == False):
            attempt = input("Attempt " + str(attempts+1) + ": ")
            if ((len(attempt) == WORD_LENGTH) and (attempt.isalpha())):
                if (attempt in DICTIONARY):
                    validAttempt = True
                else:
                    print("Invalid attempt: Please enter a real word.")
            else:
                print("Invalid attempt: Please enter a 5-letter word.")
        attempt = attempt.lower()
        attempts += 1
        solved = feedback(attempt)

#Run
if __name__ == "__main__":
    play()



#################                   NOTES                      ###############

#Could implement hard mode later but that's a later problem lol
#Dictionary returns 10230 5-letter words
#Oh you could also do a hint mode where you can be like what letters do I have in place, what letters do I have in what possible places

#Possible Data Structures:
#   1. Array of 5 Arrays [place[possible letters]]
#   2. Array of 26 tuples [letter(in word(bool), possible places[int])]
#   3. Array of 26 lists [letter[(1, 2, 3, 4, 5)] (all bool)
#       If 1,2,3,4,5 are all false, remove that letter? But then you would need
#       a way to keep track of which one is which letter, so back to tuples