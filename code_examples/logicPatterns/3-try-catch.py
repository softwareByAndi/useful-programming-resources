from helperFunctions import narrate
  
narrate([
  "we like it when our program tells us when it's not working correctly",
  
  "try inputing something that's not (y/n) and see what happens"
])

try:
  userInput = input("do you accept? (y/n) : ")
  if userInput == "y":
    print("you accepted!")
  elif userInput == "n":
    print("aww, you declined...")
  else:
    raise Exception("invalid input")
except Exception as e:
  print('-- an error has occurred --')
  print('Error: ', e)

narrate([
  "using a try-catch block, we can catch and handle errors without exiting the program"
])

# let's look at another case using the try-catch block
# see 4-try-parse.py