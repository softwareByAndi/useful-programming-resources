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

  "default": "this article has no status",
  "asdf": "you're lazy..."
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
    for status in validStatuses:
      if userInput in validStatuses[status]:
        chosenStatus = status
        break
    print(" >", statusMessages.get(chosenStatus, statusMessages['asdf']))
    print("")
except StopIteration:
  pass

narrate([
  "exiting program"
])
