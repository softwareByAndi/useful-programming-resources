# things to cover
- most common mistakes
- programming design tricks for bug free code
- programming implementation tricks for bug free code

## most common mistakes:

1. if you want to use a function, you have to `call` it.
2. if you want to run a block of code, make sure that the code you want to run is `in` that block
3. if you want to use data returned from a function, you have to `store that return value` somewhere
    - e.g. you have to assign the function's return value to a variable, then you can use that variable

## programming implementation tricks for bug free code

use a unique naming pattern to differentiate between globals, constants, parameters and local variables

### there are several advantages to this:
1. the scope of the data used is easy to read and understand `at a glance`
2. until we understand scope intuitively, this helps us not mix up our variables and use a local variable when we meant to use a global variable
3. while learning, this helps us think about which data -- (belonging to which scope) -- we are trying to access.

e.g. 
```python
G_MY_GLOBAL_CONSTANT = "this data should never change"
g_myGlobalVariable = "some global data"

def myFn(p_myParam):
    l_myLocalVariable = "some local data"
    
    global g_myGlobalVariable  
    # in python, any time we intend to use a global variable (whether the code works or not without this line), we need to add this global call.
    # not only does this call prevent us from accidentally creating a new local variable, it's also a reminder that the data we're working with is global.
    print(g_myGlobalVariable)
    print(l_myLocalVariable)
    print(p_myParam)
```
the advantage is that when everything have similar names, we know exactly which variable we're accessing:
```python
global g_data  # always do this in python (unless you're in the global scope)
print(g_data)
print(l_data)
print(p_data)
```
another option is to use `dictionaries/objects` to specify a `namespace/scope`
```python
globals = {
    "data": "some global data"
}

# note here that for parameters in particular, we prefer listed params v.s. generic objects: this is so that we can tell at a glance what this function needs to work properly
def myFn(p_data, p_myParam2):
    locals = {
        "data": "some local data"
    }
    global globals  # always do this in python
    print(globals['data'])
    print(locals['data'])
    print(p_data)
    print(p_myParam2['data'])

temp = {
    "data": "some temp data"
}
myFn("some param", temp)
    doSomethingWith(p_myParam2)
```

the last option is to specify your global variables `in a separate file/module` and `import` them as needed -- `(note that we are still using our scope naming patterns)`

```python
# globals.py
data = "some global data"
globalVariable2 = "some other global data"
```

```python
# main.py
def myFn(p_data):
    l_data = "some local data"
    from globals import data as g_data
    print(g_data)
    import globals
    print(globals.globalVariable2)
    print(l_data)
    print(p_data)

myFn("some param")
```



## implementation patterns for bug free programs:

0. implement each part of your code in a test file first
    - when testing similar code back to back, make a small change to ensure that the code that runs is the code you intended to run (i.e. you forgot to save, and you're running the previous file before it was edited.)
    - make sure to also test your new code in the same scope that you eventually want it to be in.

<br>

1. write out what you want to happen in "plain english" (or your native language)

2. draw a flow diagram of your logic
    - implement each step / block / scope `separately`
    - then use that diagram, to `assemble / puzzle together` your program
    - always verify that the new code / puzzle block that you assemble into in your main program is:
        1. in the right place (indentation & location)
        2. has everything it requires to run:
            - parameters have been passed
            - global variables exist
            




# test code:

## functions

```python
def anotherFn(myParam):
    print("executing anotherFn()")
    print("my parameter is: ", myParam)
    return "some data"
    
def myFn():
    print("executing myFn()")
    return anotherFn

fn = myFn()
myData = fn("some param data")

print("my returned data is: ", myData)
```

```python
def anotherFn(myParam):
    print("executing anotherFn()")
    print("my parameter is: ", myParam)
    return "some data"
    
def myFn():
    print("executing myFn()")
    retVal = anotherFn("some param data")
    return retVal + "!!!"

myData = myFn()
print(myData)
```

```python
def myFn():
    print("executing myFn()")
    def myInnerFn():
        print("executing myInnerFn()")
        print("asdf")
    return "inner Data"  # INCORRECT! make sure that ALL the code you want to run is inside of the block!
    myData = myInnerFn()
    return myData + "!!!"

print(myFn())
```

## scope
