from helperFunctions import narrate

narrate([
  "switch statments are powerful tools for determining the flow of logic",
  "let's look at how to implement on in python",
  "", 
  "unfortunately python doesn't have a switch statement,",
  "but we can fake one using a dictionary",
  "",
  "the dict.get() method takes 2 parameters: a key and a default value",
  "the default value is used should the dictionary not contain an entry for the given key.",
  "",
  "take a look at this code, and see what happens when you enter invalid input"
])

statusMessages = {
  "PUBLISHED": "this article is published",
  "DRAFT": "this article is a lowly draft",
  "ARCHIVED": "this article has been archived",
}

validStatuses = {
  "PUBLISHED": ['p', 'P', 'published', 'Published', 'PUBLISHED'],
  "DRAFT": ['d', 'D', 'draft', 'Draft', 'DRAFT'],
  "ARCHIVED": ['a', 'A', 'archived', 'Archived', 'ARCHIVED'],
}

quit = ['q', 'Q', 'quit', 'Quit']

try:
  while True:
    userInput = input("select a status: (PUBLISHED, DRAFT, or ARCHIVED) : ")
    if userInput in quit:
      raise StopIteration
    chosenStatus = None
    for key in validStatuses:
      if userInput in validStatuses[key]:
        chosenStatus = key
        break
    print(" >", statusMessages.get(chosenStatus, "invalid input '" + userInput + "'..."))
    print("")
except StopIteration:
  pass

narrate([
  "exiting program"
])


# we can also set a default value for our switch statment
# see 14-switch-default.py