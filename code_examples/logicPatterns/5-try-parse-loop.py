from helperFunctions import narrate


narrate([
  "try inputing something that's not a number and see what happens"
])


userInput = None
print("pick a number, any number... : ", end="")
while userInput == None:
  userInput = input("")
  try:
    userInput = int(userInput)
  except ValueError:
    userInput = None
    print("hmm, that wasn't a number... try again: ", end="")

print("you picked :", userInput, "!")


narrate([
  "using a loop, we can easily re-prompt for valid input before continuing our program"
])


# first we're printing out our prompt, then inside our loop we wait for user input
# if we are unable to parse the input, we re-prompt and try again until the user enters valid input

# ---------------------------------------------

# why don't we prompt for input inside the loop?
# if we want the same prompt every time, then that's a valid option
# however I don't like poluting the user interface with uneccessary text

# let's try using this pattern with other forms of validation
# see 6-try-parse-loop-string.py