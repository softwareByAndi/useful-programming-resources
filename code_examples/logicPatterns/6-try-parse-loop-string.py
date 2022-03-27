from helperFunctions import narrate

narrate([
  "try inputing something that's not (left/right) and see what happens"
])


userInput = None
print("would you like to go left or right? (left/right) : ", end="")
while userInput == None:
  userInput = input("")
  try:
    if userInput not in ['left', 'right']:
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

# but typing a full word is tedious, I also want to give players the ability to type shortcuts

# see 7-try-catch-parse-input-loop.py