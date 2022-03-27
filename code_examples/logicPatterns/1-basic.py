# basic if statement
from helperFunctions import narrate

narrate([
  "a basic if statment program.",
  "try typing something that's not (y/n) and see what happens"
])

userInput = input("do you accept? (y/n) : ")
if userInput == "y":
  print("you accepted!")
else:
  print("aww, you declined...")

narrate([
  "exiting program..."
])

# this is fine for simple tasks, 
# but how should we define what happens when we input something that's not 'y' or 'n'?

# see 2-invalid-input.py