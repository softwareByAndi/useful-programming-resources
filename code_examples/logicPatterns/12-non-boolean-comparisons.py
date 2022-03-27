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


try:
  while True:
    inputArray = input("type anything you want: ")
    inputList = inputArray.split("|");
    for userInput in inputList:
      if userInput in quit:
        raise StopIteration # semantic exception to break out of nested loops

      if userInput in null:
        respond(userInput, "you entered a Null value!")
        # notice here that null inputs also output "you typed the text..."
        # sometimes this behavior is desired, and can be implemented simply
        # by neglecting an else clause

      try:
        respond(userInput, responses_switch[userInput])
      except KeyError:
        try:
          respond(userInput, "you typed the number: ", int(userInput))
          raise StopIteration
        except ValueError:
          respond(userInput, "you typed the text: '" + userInput + "'")

    print("")
except StopIteration:
  pass

narrate([
  'exiting the program...'
])


#
# switch statements are powerful tools, let's take a look at some more examples
# see 13-switch.py