from helperFunctions import narrate

narrate([
  "in this program, we only print 'SUCCESS!' if an exception isn't thrown",

  "in other words, only if the code before it completes without any errors",

  "try inputing something other than a number and see what happens"
])


def parseUserInput(userInput):
    parsedInt = int(userInput)
    return parsedInt * 100

def parseInput2(userInput):
    try:
        userInput = parseUserInput(userInput)
        print("SUCCESS! you entered:", userInput)
    except ValueError:
        print("'" + userInput + "' is not a number. try again: ", end="")
        userInput = None

userInput = None
print("pick a number, any number... : ", end="")
while userInput == None:
  userInput = input("")
  parseInput2(userInput)


narrate([
  "sometimes, we can simplify our code by handling some logic in the caller,",

  "instead of in the function itself"
])


# by now you're probably wondering what you can and cannot compare
# so let's move on to non-boolean comparisons

# ---------------------------------------------

# see 11-truthy-and-falsy-values.py
