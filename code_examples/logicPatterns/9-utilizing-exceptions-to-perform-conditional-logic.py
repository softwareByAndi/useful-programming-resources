from helperFunctions import narrate

narrate([
  "in this program, we only print 'SUCCESS!' if an exception isn't thrown",
  "in other words, only if the code before it completes without any errors",
  "try inputing (pass/fail) and see what happens"
])


userInput = input("does this test pass or fail? : ")
try:
  if userInput not in ['pass', 'Pass', 'p', 'P']:
    raise ValueError
  print("SUCCESS")
except ValueError:
  print("FAILURE")


narrate([
  "in this way, exceptions can be used in a similar way to if/else logic"
])


# why might we want to use an exeption like this instead of just using if/else?
# for semanic reasons : if there's an error in our code, then we should say there's an error.
# In most cases, we might prefer to use if/else;
# but occasionally we'll want to handle an error outside of a function. 
# in cases such as that, exceptions are a simple way to implement that logic.

# ---------------------------------------------

# let's see how exceptions can be used to perform logic in functions

# see 10-exceptions-in-functions.py
