# Random number guesser game
import time
import random

Number = random.randint(1,100)
attemps = 0

print("Loading...")
time.sleep(1)
print("\nWelcome to the Number Guessing Game!\n")
print("---------------------------------------")
print("Rules :")
print("\nChoose a number between 1-100.")
print("You need to guess the correct number to win!\n")
print("---------------------------------------")

while True :
  guess=(input("Choose a Number: "))

  if not guess.isdigit() :
    print("Loading...")
    time.sleep(1)
    print("---------------------------------------")
    print("Please choose an Valiad Number")
    print("---------------------------------------")
    continue

  guess =int(guess)
  attemps += 1

  if guess > 100 or guess < 1 :
    print("Please chose a number between 1 - 100")

  if  guess > Number :
    print("----------------------------------------")
    print("Checking the number...")
    time.sleep(1)
    print("\nThe Number is lower,")
    print("----------------------------------------")
  elif guess < Number :
    print("----------------------------------------")
    print("Checking the number...")
    time.sleep(1)
    print("\nThe Number higher,")
    print("----------------------------------------")
  elif guess == Number :
    print("----------------------------------------")
    print("Checking the number...")
    time.sleep(2)
    print(f"\nCorrect! , You guessed the number [{Number}] in {attemps} attempts!")
    print("----------------------------------------") 
    agian = (input("Do you want to play agian? (yes/no): ")).lower()
    print("----------------------------------------")

    if agian == 'yes' :
     print("Repearing the game...")
     print("----------------------------------------")
     time.sleep(2)
     Number = random.randint(1,100)
     attemps = 0
     continue
    elif agian == 'no' : 
     time.sleep
     print("\nThanks for playing...")
     break   
 

  
