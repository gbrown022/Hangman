# Geoffrey Brown
# July 19, 2019
# v0.01 July 24, 2019

import random
import string

#print('wordsList len() is: ' + str(len(wordsList)))
# replace with a function pulling a word from TBD
wordsList = ["apple", "boxer", "chamomile", "dragon", "energy", "frumpy"]
userGuessSuccess = False
maxGuesses = 10
# using string to define a list of the ascii lowercase alphabet
alphabet = list(string.ascii_lowercase) 

def getSecretWord(list):
    # select a random word
    randPosition = random.randint(0,(len(wordsList)-1))
    return(wordsList[randPosition])

def fillHyphens(puzzleWord):
    blankedPuzzle = ""
    for i in range(len(puzzleWord)):
        blankedPuzzle += '-'
    #print('blankedPuzzle = ' + blankedPuzzle)
    return(blankedPuzzle)

def replaceLetters(letter, solution, displayWord):
    s = list(displayWord)
    for index in range(len(solution)):
        if (solution[index] == letter):
            s[index] = letter
    return("".join(s))

# main loop
def guess(word):
    guessCount = 0
    alreadyGuessed = []
    displayWord = fillHyphens(word)

    while guessCount < maxGuesses:
        if ((len(alreadyGuessed)) > 0):
            print('You have previously guessed: ' + ', '.join(alreadyGuessed))
        
        print('The puzzle word looks like: ' + displayWord)
 
        letter = input('Guess a letter in the secret word: ').lower()

                
        if not letter in alphabet:
            print('Enter a letter a-z.')
        elif letter in alreadyGuessed:
            print('You have already guessed that. Try again.\n')
        else:
            if letter in word:
                displayWord = replaceLetters(letter, word, displayWord)
                print('You guessed a letter in the secret word: ' + displayWord + '\n')
                if (displayWord == word):
                    print("You win!")
                    return
            else:
                alreadyGuessed.append(letter)
                guessCount+=1
                print('Uh oh. Incorrect guess number: ' + str(guessCount) + '\n')        

secretWord = getSecretWord(wordsList)

# game loop executed with the next statement
guess(secretWord)
print('The secret word was: ' + secretWord)