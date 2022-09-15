from secrets import choice
import random

computer= random.choice(["rock", "paper", "scissors"])
user=input("rock, paper or scissors?")
print("The computer chose", computer,"and the user chose", user +".")
if user==computer:
    print("Try again")
if user=="Rock" and computer== "paper" :
 print("You lose")
elif user=="paper" and computer== "scissors": 
 print("You lose")
elif user=="paper" and computer == "rock":
    print("You win")
elif user== "rock" and computer== "scissors": 
    print("You win")
elif user== "scissors" and computer== "paper":
    print("You win")
elif user== "scissors" and computer== "rock":
    print("You lose")

