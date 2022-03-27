from helperFunctions import narrate
  
narrate([
  "we like it when our program tells us when it's not working correctly",
  
  "try inputing something that's not a number and see what happens"
])

userInput = input("pick a number, any number... : ")
try:
  userInput = int(userInput)
  print("you picked : ", userInput, "!")
except ValueError:
  print("hmm, that wasn't a number...")

narrate([
  "using a try-catch block, we can catch and handle errors without exiting the program"
])

# notice that instead of catching all errors, 
# we're now catching only ValueError exceptions

# this is important, because what if we get an exception caused by 
# something other than an error? in this case I want our program to freak out

# ---------------------------------------------

# why don't we simply catch all exceptions?
# because we only want to catch the errors which we are expecting to be thrown.
# unexpected errors lead us to bugs in our code, 
# but if we were to handle them silently then we won't be informed of possible bugs which need fixing

# ---------------------------------------------

# this pattern works well in loops too
# see 5-try-parse-loop.py