def myPrint(str):
  print(str)
  myVar = "myVar"
  # return str + "!!!"
  def myFn():
    print(myVar)
    return myVar
  return myFn

mydict = {
  "fn1": lambda: myPrint("fn1"),
  "fn2": lambda: myPrint("fn2"),
  "fn3": lambda: myPrint("fn3"),
}
  
def narrate(lines):
  print("")
  l1 = [mydict[key]()() for key in mydict]
  
  print("")
  return l1

l = narrate([
  "hello",
  "world"
])


print("l: ", l)
