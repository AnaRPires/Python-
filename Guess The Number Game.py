#AnaPires
#HLT's 3)
#Guess the Number Game
import random # imports the random library
print ("\n\tHello and welcome to the guess your number game \n\n")
# Function that asks the user to enter a name
#          and displays a greeting
myName = input("Hello! What is your name? ")
number = random.randint (1,20) # random generation between 1 and 20 
#print(number)
print("Well, " + myName + " I am thinking of a number between 1 and 20.")
# end of function
guessesTaken = 0

while guessesTaken < 6:
  guess = int(input("Take a guess: "))
  
  guessesTaken = guessesTaken + 1
  if guess > number:
    print("That was too high!")
  elif guess < number:
    print("That was too low!") 
  else:
    break  
if guess == number:
  print("Great job, " + myName + " you guessed my number!")
else:
  print("Wrong, better luck next time")  


  
