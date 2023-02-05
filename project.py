import speech_recognition as sr
import random
from time import sleep

WORDS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
GUESS = random.choice(WORDS)
MAX_GUESSES = 3
guess = 1

#Instantiating the recognizer and microphone
r = sr.Recognizer()
mic = sr.Microphone()

print("Choose a word from 'red, orange, yellow, green, blue, indigo, violet'")
print("You have 3 guesses!")
sleep(2)
mode = input("Do you wish to use microphone or an audio file?\n Enter '1' to use microphone\n Enter '2' to use audio file \n")
if mode == "2":
    while guess < 4:
        print(f"Guess {guess}")
        guess+=1
        file_name = input("Enter the file name: ")
        my_file = sr.AudioFile(file_name)
        with my_file as source:
            audio = r.record(source)
        try:
            print(r.recognize_google(audio))
            if GUESS == r.recognize_google(audio):
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
        print(f"I was thinking of {GUESS}")

elif mode == "1":
    while guess < 4:
        print(f"Guess {guess}. Speak!")
        guess+=1
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:    
            if GUESS == r.recognize_google(audio, show_all = False):
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
        print(f"I was thinking of {GUESS}")
        
else:
    print("Invalid Entry!")
    print("Good Bye!")


    