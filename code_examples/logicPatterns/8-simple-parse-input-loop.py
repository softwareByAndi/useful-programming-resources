from helperFunctions import narrate

narrate([
  "in this program, we give the user multiple ways to select the same option",

  "try inputing something ('l', 'L', 'r', 'R', 'Left', or 'Right') and see what happens"
])


options_left = ["left", "Left", "l", "L"]
options_right = ["right", "Right", "r", "R"]

userInput = None
print("would you like to go left or right? (left/right) : ", end="")
while userInput == None:
  userInput = input("")
  if userInput in options_left:
    userInput = 'left'
  elif userInput in options_right:
    userInput = 'right'
  else:
    print("invalid input: '" + userInput + "' you can only move left or right... try again: ", end="")
    userInput = None

print("you move ", userInput + "!")


narrate([
  "using a loop, we can easily re-prompt for valid input before continuing our program"
])


# first we're printing out our prompt, then inside our loop we wait for user input
# if the input is not a valid option, we re-prompt and try again until the user enters valid input

# ---------------------------------------------

# when might we prefer using a try-catch over an if else then?
# 1. when we want to handle a likely to be thrown exception without exiting the program
# 2. when we only want to run some code should the code before it execute successfully without throwing exceptions

# let's take a closer look at this 2nd case
# see 9-utilizing-exceptions-to-perform-conditional-logic.py