def choose_path():
    print("hello")
    print("which room do you wish to enter?")
    
    # unless this is a niche exploration game (as in the player doesn't know what they can do unless they type it)
    # it's always helpful to tell our player what their choices are and how to choose them
    
    '''
    below we defined some variables 'option_left', 'option_right', and 'option_quit': this is called programming semantically.
    programming semantically is the practice of giving meaningful names to our variables
    and in this case, it allows us to easily redefine the values of our input options by only changing one part of the code
    
        otherwise we have what are called "magic numbers" (or in this case "magic text options") 
        magic numbers are numbers with no semantic meaning attached
        
        an example of magic numbers could be:
        >   x = 3.14159 * 17 ** 2
        
        unless we're already very familiar with that equation, it's very difficult to tell what sort of logic is being performed
        if we were to program the same equation using semantic variable names, it would look like this:
        >   pi = 3.14159
        >   radius = 17
        >   def squared(num): return num ** 2
        >   area = pi * squared(radius)
        
        isn't that much easier to understand? especially if you're not the one who wrote the code
        
        technically we still have a magic number here. (the 2), but it's easy to understand logically where this number came from,
        so it's fine to leave it as is.
    '''
    
    option_left = '0'
    option_right = '1'
    option_quit = 'quit'
    print("  (" + option_left + ") : take the room to the left")
    print("  (" + option_right + ") : take the room to the right")
    
    # people type stuff in wrong all the time. it's always helpful to be prepared for anything the user might input at any given time
    # the following loop pattern is an easy way to handle that.
    # as with every loop, we must define an end case. in this case we want to continue the loop until the user enters a valid input.
    # for this case, we'll define any invalid input as None, but this can be anything
    playerInput = None
    while playerInput == None:
        playerInput = input("")
        # using our semantic variables 'option_left, option_right & option_quit' it's easy to understand what part of the code we're in,
        # while still retaining the convenience and option to easily change what the user must input to choose any given path. 
        if playerInput == option_left: 
            print("you enter the room to the left")
        elif playerInput == option_right:
            print("you enter the room to the right")
            
        # it's important to always give the player a way to quit the application
        elif playerInput == option_quit:
            # we can also implement save logic here... e.g.:
            # save_game()
            print("exiting game...")
            quit()
        else:
            print("that's not an option")
            # if we've entered this code, then the player entered an invalid input. 
            # so let's make sure to reset our playerInput variable to None so that our input loop continues.
            # (or to whatever we defined invalid input to be)
            playerInput = None
        
        
choose_path()

# program output
'''
hello
which room do you wish to enter?
  (0) : take the room to the left
  (1) : take the room to the right
1
you enter the room to the right
'''

'''
hello
which room do you wish to enter?
  (0) : take the room to the left
  (1) : take the room to the right
quit
exiting game...
'''
