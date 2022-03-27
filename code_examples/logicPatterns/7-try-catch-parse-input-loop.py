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
  try:
    if userInput in options_left:
      userInput = 'left'
    elif userInput in options_right:
      userInput = 'right'
    else:
      raise ValueError("invalid input: '" + userInput + "' you can only move left or right...")
  except ValueError as e:
    userInput = None
    print(e, "try again: ", end="")

print("you move ", userInput + "!")


narrate([
  "using a loop, we can easily re-prompt for valid input before continuing our program"
])


# first we're printing out our prompt, then inside our loop we wait for user input
# if the input is not a valid option, we re-prompt and try again until the user enters valid input

# ---------------------------------------------

# we don't technically need to use a try-catch block for this though. 
# we can simplify to just an if-else statement

# see 8-simple-parse-input-loop.py