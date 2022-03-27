from operator import truth
from helperFunctions import narrate

narrate([
  "in order to make a comparison, we need something that's either true or false",
  "in a simple system, this is done just using booleans: True/False",
  "but in more complicated systems, having only these booleans is rather restricting;",
  "",
  "so we added boolean operators: (==, !=, !, >, <, etc...).",
  "using these operators, we can receive a boolean (true/false) value when comparing 2 values.",
  "and while this alone allows us to perform any logic we need,",
  "it's still convenient to have one more operator;",
  "",
  "that is, all values should have the ability to be coerced into a truthy or falsy boolean value",
  "what this means is that every value can be used just like a boolean;",
  "",
  "------------------------------------------------",
  "",
  "in this script we take a look at values which evaluate to truthy or falsy",
  "and identify which is which"
])

def truthy_or_falsy(val):
  if val:
    print("truthy", end=": ")
  else:
    print("falsy", end = ":  ")
  print("'" + str(val) + "'")

truthy_or_falsy({})
truthy_or_falsy([])
truthy_or_falsy(None)
truthy_or_falsy(())
truthy_or_falsy( (0) ) # look carefully at me! tuples with a single value are coerced into just the value
truthy_or_falsy(set())
truthy_or_falsy("")
truthy_or_falsy(range(0))

print("")

truthy_or_falsy("hello world")
truthy_or_falsy({"hello": "world"})
truthy_or_falsy((0, 0))
truthy_or_falsy((0, 1))
truthy_or_falsy(([0]))
truthy_or_falsy([0, 1])
truthy_or_falsy(range(1))
truthy_or_falsy(range(3))

print("")

truthy_or_falsy(0)
truthy_or_falsy(0.0)
truthy_or_falsy(0j)
truthy_or_falsy(1)
truthy_or_falsy(1.0)
truthy_or_falsy(1j)
truthy_or_falsy(200)
truthy_or_falsy(-1)

narrate([
  "this behavior is most often used to easily check if a value is empty",
  "but note that not all languages treat values the same way",
  "",
  "for instance in javascript: {} and [] (empty dictionaries and lists)",
  "are actually truthy values, not falsy",
  "",
  "and C++ only coerces numerical values into truthy or falsy.",
  "Although more complicated boolean coersion can easily be implemented case by case"
])