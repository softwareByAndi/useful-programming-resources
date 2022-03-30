# Debugging Tutorial Script:

[link to tutorial recording here](https://www.youtube.com/watch?v=4-Um9BovATo)

<br>

# intro
It's inevitable that as programmers we've written some code that behaves unexpectedly, 
and even after combing through our code, we just can't understand why.

This tutorial is designed to provide us with fundamental debugging techniques for just these occasions.

<br/>

# typos and other silly mistakes
The first thing I always recommend is to comb through your code and make sure there aren't any silly mistakes.
Bugs that make our program crash, are most often caused by typos. these bugs will likely cause an `Exception` to be thrown which make identifying them and fixing them an easy task. (so long as we don't accidentally silently handle such exceptions)

<br>

# logical errors
more difficult bugs are cause by correct syntax, but poor or careless logic on the developer's behalf. A common example of such bugs is to use or pass the wrong variable. Such bugs are very common when refactoring. another example of such a bug is to perform a similar but incorrect operation.

### for example:
```python
cube(num): return num * 3   # incorrect
cube(num): return num ** 3  # correct
```
<br/>

what makes logical bugs difficult to find is that syntactically they are perfectly valid; and typically only present themselves through inconsistent, unexpected &/or undefined behavior in our program. these bugs typically don't throw exceptions, and when an exception is thrown, it's often in a location unrelated to the logical error which caused it.

there's no easy way to find some of these bugs, but there are techniques which are more reliable than others.
The first of which is simply to read the code and logically consider the execution of the program line by line. But, what if we have lot of code? it doesn't make sense to read through thousands of lines of perfectly fine code, so first let's attempt to identify the rough location of the bug.

<br>

## block tags
for bugs that crash our code, this is easy. simply tag a few logs or print statements at the beginning of each major block of your code. -- the last statement to have logged to your console before the app crashed will identify the block of code that's breaking.
if the identified block is too big to comb through, repeat the same tactic by tagging a log or print statment infront of each of the major sections of the incriminated block of code. -- the last statement to have logged to your consol before the app crashed will identify the block of code that's breaking.

rinse and repeat until you've narrowed a small enough section to comb through visually. a visual review of a targeted section of code is usually enough to consistently find the typo or logical error.

But what if the code looks fine? it's typo free, and logically sound. Now is the point where we need to start looking at the values of the data we're working with.

<br>

## logging scoped values
before we get into any debugging tools designed for this task, let's hoof it with good ol' logs & print statements

now that we've identified the code that's breaking, let's refactor our current logs to include any data the current scope uses or interacts with.

We will then need to cross compare the data we see here with what the program is expecting.

<br>

what's that? all of the data looks correct? that's good to hear, but are you sure?
- try logging the type of data being passed in as well. is the number you're reading actually a number? or is it a string that just looks like a number when you print it out?

<br>

## back-tracing
hopefully by now we've identified the offending variable that is breaking our code. Sometimes we're lucky and we know exactly what went wrong, but let's pretend we're not so lucky today.

Our next task is to track the source of the offending variable. Let's take a look at the data that's used to initialize the offending variable. If this data looks correct, and the initial value of the offending variable isn't suspect, then the bug might lie somewhere between the offending variable's initialization and the point where the program crashes.

We can use print statements as a useful but somewhat inconvenient method of tracing its value throughout its lifetime.

note though, that just because this data appears correct, doesn't actually mean that it is. let's look at some more robust methods of debugging.

<br>

## testing & verification
the best and easiest way to ensure that our code always runs correctly is to write tests. We will select individual functions to test before testing larger parts of the program. This is so that we can confirm each cog works correctly before assembling it into the machine.

A test is simple, if not a little tedious. first define expected output for a series of expected and unexpected inputs, then run the function to be tested using the defined inputs while comparing the function's results the the expected values. If these don't match up, then we've identified a bug in our code.

for small programs, writing a test for every function is more work than it's worth. So for now, although we really should thoroughly test our code in this way, we'll save the robust testing for production code and only bother testing the functions for which we believe a bug exists.

<br>

# debugging tools
many tools exist for the express purpose of debugging our code, and every major IDE has a built in debugger. Luckily these are all very similar to each other. Some of them get very detailed, but they all have the same main features:
1. breakpoints --> ( pause execution here )
2. step over --> ( next line )
3. step into --> ( dive into the next scope )
4. continue --> ( resume execution until the next break point )
6. scope & variables --> ( read the current value of any variable visible from within the current scope of execution )
5. exit --> ( stop execution and terminate the program )

<br>

## debugging in the console:
We don't necessarily need an IDE to debug our code though. we can also find a number of debugging tools which can be used right in the console.

[An Introduction To Python Debugging with the PDB -- a YouTube tutorial by TutorialEdge](https://www.youtube.com/watch?v=VQjCx3P89yk)

<br>

# defensive programming
truly the best way to find and prevent bugs is to program defensively, but what does this mean?

>Defensive programming stands for the use of guard statements and assertions in your code base. ... This technique is designed to ensure code correctness and reduce the number of bugs.
[-- "defensive programming" by Vladimir Khorikov](https://enterprisecraftsmanship.com/posts/defensive-programming/)

There are 2 widely spread forms of defensive programming. these are `Pre-Conditions` & `Assertions`. In practice, they're nearly identical -- they both confirm/assert that the data is correct, and they both stop program execution should that not be the case.

there is a slight nuance between the two though: 

- where pre-conditions check that the value of data falls within a permissible range, assertions typically confirm that the structure of data follows the expected format.

- and where pre-conditions typically fall BEFORE the execution of some logic, assertions typically execute AFTER some logic has been performed, & BEFORE the resulting data is to be used elsewhere in the program.

- in other words: pre-conditions confirm the validity of data we've received, while assertions confirm the validity of data we send away.

In summary though, defensive programming is the art of verifying values are correct at any given point within the program's execution, and to halt execution with descriptive error messages should data not fall within the expected range, be structured incorrectly, or even be the wrong type of data entirely

In this way, our code is guaranteed to always be working with valid data which significantly decreases the number of bugs in our code.

If you're curious and want to learn more about this, I highly recommend reading Vladimir's introductory article on the topic -- ["Defensive Programming: the good, the bad & the ugly"](https://enterprisecraftsmanship.com/posts/defensive-programming/).
