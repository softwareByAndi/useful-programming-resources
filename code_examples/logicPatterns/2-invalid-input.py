from helperFunctions import narrate
  
narrate([
  "we like it when our program tells us when it's not working correctly",
  "try inputing something that's not (y/n) and see what happens"
])

userInput = input("do you accept? (y/n) : ")
if userInput == "y":
  print("you accepted!")
elif userInput == "n":
  print("aww, you declined...")
else:
  raise Exception("invalid input")

narrate([
  "exiting program..."
])

# now our program can identify when a user inputs something unexpected, 
# but sometimes we don't want to end our program to end quite yet.
# in these cases, we can use a try-catch block

# see 3-try-catch.py