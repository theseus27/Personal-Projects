import time
try:
    from nltk.corpus import words as dictionary
except:
    try:
        import nltk
    except:
        import subprocess
        subprocess.run(['pip', 'install', 'nltk'], stdout=subprocess.DEVNULL)
        import nltk
    nltk.download('words')
    from nltk.corpus import words as dictionary
    
    
def setWordle():
    start = time.time()
    impossible = ['a', 'd', 'e', 'h', 'r', 's', 't']
    dictionarySet = set()
    for word in dictionary.words():
        dictionarySet.add(word)

    for i in range(97, 123):
        if (i in impossible):
            continue
        for j in range(97, 123):
            if (j in impossible):
                continue
            word = str(chr(i) + "e" + chr(j) + "ra")
            if (word in dictionarySet):
                print(word)

    end = time.time()
    print("Runtime: ", end-start)


def listWordle():
    start = time.time()
    impossible = ['a', 'd', 'e', 'h', 'r', 's', 't']

    for i in range(97, 122):
        if (i in impossible):
            continue
        for j in range(97, 122):
            if (j in impossible):
                continue
            word = str(chr(i) + "e" + chr(j) + "ra")
            if (word in dictionary.words()):
                print(word)

    end = time.time()
    print("Runtime: ", end-start)

#setWordle()
#listWordle()

def nextSetWordle():
    possible = ['b', 'f', 'i', 'j', 'k', 'l', 'm', 'v', 'x', 'z']
    dictionarySet = set()
    for word in dictionary.words():
        dictionarySet.add(word)
    
    for i in range(97, 122):
        i = chr(i)
        if ((i not in possible) or (i == 'i')):
            continue
        for j in range(97, 122):
            j = chr(j)
            if (j not in possible):
                continue
            for k in range(97, 122):
                k = chr(k)
                if ((k not in possible) or (k == 'l')):
                    continue
                for l in range(97, 122):
                    l = chr(l)
                    if ((l not in possible) or (l == 'l')):
                        continue
                    
                    word = str(i + j + k + l + "o")
                    
                    if ((word in dictionarySet) and ('l' in word) and ('i' in word)):
                        print(word)
nextSetWordle()