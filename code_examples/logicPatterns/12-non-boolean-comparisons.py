from helperFunctions import narrate

null = ['none', 'None', 'undefined', 'null', 'Null', 'NULL']
quit = ['q', 'Q', 'quit', 'Quit', 'quit()', 'Quit()']
responses_switch = {
  "hello": "greetings, my child. I am World",
  "world": "you called?, how can I help you?"
}

narrate([
  "now lets investigate some methods of advanced non-boolean-comparisons",
  "",
  "valid values for this program include:",
  "",
  "any number",
  "any text",
  "[" + ", ".join(responses_switch.keys()) + "]",
  "[" + ", ".join(null) + "]",
  "[" + ", ".join(quit) + "]"
])

def respond(*args): 
  print("'" + str(args[0]) + "'", ">", *args[1:])

# whileLoop
loopName = "whileLoop"
try:
  while True:
    inputArray = input("type anything you want: ")
    inputList = inputArray.split("|")
    
    # forLoop1
    loopName = "forLoop1"
    try:
      for userInput in inputList:
        if userInput in quit:
          raise StopIteration("whileLoop")  # semantic exception to break out of nested loops
  
        if userInput in null:
          respond(userInput, "you entered a Null value!")
          raise StopIteration("forLoop1")
          # notice here that null inputs also output "you typed the text..."
          # sometimes this behavior is desired, and can be implemented simply
          # by neglecting an else clause
  
        if responses_switch.get(userInput, False):
          respond(userInput, responses_switch[userInput])
        else:
          try:
            respond(userInput, "you typed the number: ", int(userInput))
          except ValueError:
            respond(userInput, "you typed the text: '" + userInput + "'")
            
    except StopIteration as e:
      print("error handling: ", loopName)
      print("error type: ", type(e))
      error = str(e)
      
      if error != "forLoop1":
        print("'" + str(e) + "' : '" + str(loopName) + "'")
        raise StopIteration(error)
      pass
      
    print("")
except StopIteration as e:
  print("error handling: ", loopName)
  print("error type: ", type(e))
  error = str(e)
  
  if error != "whileLoop":
    print("'" + str(e) + "' : '" + str(loopName) + "'")
    raise StopIteration(error)
  pass

narrate([
  'exiting the program...'
])


#
# switch statements are powerful tools, let's take a look at some more examples
# see 13-switch.py