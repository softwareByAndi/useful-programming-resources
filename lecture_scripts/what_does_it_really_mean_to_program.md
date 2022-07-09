# start with QA

** start recording **

# what does it mean to program?

to program is to define a set of instructions which tell someone, or something what to do and when to do it.

- for example, if I were to program my secretary, then I can give some rather vague instructions of what I want done, when I need it finished by, and he will be able to figure out how or in what way to complete the task.

- but computers are dumb. They will do exactly what you tell them to do, and sometimes we tell them to do some pretty silly/dumb stuff. So as programmers it's our job to be meticulous in providing detailed and comprehensive instructions to our programs / systems
- I'll repeat that: as programmers it's our job to be meticulous in providing __detailed__ and __comprehensive__ instructions to our programs / systems

and what developed out of the need for such comprehensive control was actually __a very simple system__. We created and defined hardware infrastructure which takes and __executes 1 instruction at a time__, and all it does is __add__, __multiply__ or __divide__ 2 numbers.  Of course we also need a way to __load__ and __store__ numbers, so with just those __5 instructions__ we've built the entire digital infrastructure which exists today.

note that such low level instructions are carried out __in hardware__, not in software.  

- and for those who are interested, diagrams of very simple examples of the hardware implentation can be seen on the right

- Old computers used to be programmed using physical connections. this was tedious and prone to errors, so around 1940, [John Von Neumann](https://www.britannica.com/technology/stored-program-concept) decided we should be storing this data on loadable drives, which can be read into the computer.

- this wasn't an original idea, people simply thought that loading instructions from (and to) an outside source like this would be way too slow. And it was about 100x slower than the computers of the day, but the convenience of this new design made computers easier to use than ever before.

## enter modern day, where %99.999 of all computers are now programmed by reading software instructions on external storage devices.

and so software programmers now have a job. But coding in 1's and 0's is simply outright unreasonable.

So in order for us programmers to do our jobs as easily and efficiently as possible, we defined something call Instructions &/or Commands. These are simply a method of telling the computer what to do & when to do it, using a syntax that is more readable: 

- I'll repeat that: Instructions are simply a method of telling the computer what to do & when to do it, preferably using a semantic syntax that is easily read by humans: 

- in other words, we wrapped the unreadable machine code in semantic wrappers to make it more intuitive to read and write. 
   
## enter assembly language : on the right

note that the 2 most important (and most often used) commands involve __reading and storing data__. computers have 3 locations for storage. 
1. the first being your hard drive for long term storage. Note that this is a very slow query in comparison to the other 2 storage locations...

2. the second being your (RAM) in other words your Random Access Memory for holding informaion which is used frequently. this is a much faster query, but the information here eventually needs to be written back to the harddrive should we wish to keep it for long term use.

3. the third location is a number of tiny boxes in your CPU called registers. the computer uses thes registers to hold small bits of information it's directly manipulating at any given time.

  - most tiny chips have at least 7-8 registers.
  - most bigger computers have many many more than that.


So now we have instructions for addition, multiplication, & division
and we have instructions for loading and storing data
With that, we're fully capable of telling the computer exactly what to do. But semantically it makes sense to have an instruction for jumping to a different part of code. 

- with just the above 5 instructions we can technically hack this behavior together, but this is an instruction that will be use often enough that we should just build a wrapper for it.

- Why? because at some point, we are going to write conditional logic -- we'll only want code to execute in some situations but maybe not in other situations. 

## enter the jump statement
this statement simply sets the program counter to whatever address we want.

this wrapper instruction becomes especially useful when we find the desire to repeat the same code multiple times.

Loops save us from copy & pasting the same instructions over and over, and all they are is a conditional jump statement at the end of a code.

- "are we done with the loop? if no then jump to the beginning of the loop again. otherwise, continue with the rest of the code."

<br>

by now we've covered 3 of the 4 base concepts. The last of these concepts is the most powerful of them all:

# Enter, Abstractions

**open jamboard**

Abstractions are simply wrappers which allow us to wrap &/or contain tedious, repeatable and often used code. 

- It's exactly what we did when we wrapped machine code in more semantic wrappers to create Assembly code.

- note here that the assembly language wraps machine code
- the C & C++ languages wrap the assembly language
- and the python language actually wraps the C++ language

by wrapping code which is tedious to write, difficult to read, highly repeatable or unintuitive, we create a higher level language which is more intuitive, easier to learn, and more efficient to program in.

## most commonly interfaced abstractions

as programmers and even new programmers there are a number of abstractions which you will iterface with commonly & consistently. these are Data Structures and functions. 

similar to loops, functions provide us a way to easily define reusable code. 

- this way, instead of calling a jump statement to whatever address the reusable code is located at, we can simply call the function name, and the abstraction does all of that tedious setup for us behind the scenes.

as for data structures, It's often easier to approach the design and implementation of a program using an intuitive abstractions. 

Obejcts and Structures allow us to group data which belong together. 

for example lets say I have some variables called "speed" & "size": I can wrap these variables in a wrapper named "Car", and instantly the variables make sense.

- but more importantly, now w can have multiple instances of Car, each with their own unique values for "speed" and "size" and we can treat them all as if they're the same.

### standardization 

This is an important concept/design pattern called standardization. By standardizing the format of often used tools, we can write our software in a tool-agnostic way, and it will work with any tools which follow the standardized format.


# break & QA

we'll go more in depth into design patterns later in this course.

for now, we'll take a 5 min break - grab some water and a snack or use the restroom.

- I'll open the discussion to questions when we get back


# programming agnostically :


