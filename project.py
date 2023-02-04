import speech_recognition as sr
import random
from time import sleep

WORDS = ["come", "went", "river", "tree", "sea"]
GUESS = random.choice(WORDS)
MAX_GUESSES = 3
guess = 1

r = sr.Recognizer()
mic = sr.Microphone()

print(GUESS)
print("Choose a word from 'come, went, river, tree, sea'")
print("You have 3 guesses!")
sleep(2)

while guess < 4:
    print(f"Guess {guess}. Speak!")
    guess+=1
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:    
        if GUESS == r.recognize_google(audio, show_all = False) :
            print("Correct! You won!")
            break
        else:
            print("Try Again")
            continue
    except:
        print("An error occurred")

else:
    print("You have reached the maximum amount of guesses!")
    print("Good Bye!")
    


    