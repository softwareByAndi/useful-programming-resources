def num_coins_dp(cents):
    # for testing & verification purposes, we want to store the original value of cents
    temp_cents = cents;
    
    # -------------------------------------------
    # MAIN_CODE_START
    # -------------------------------------------
    coins = [25, 10, 5, 1]
    coin_count = [0]*len(coins)
    for denom_index in range(len(coins)):
        # defining the variable 'denomination' is technically unnecessary, 
        # but defining a semantic variable like this makes the later code easier to read
        denomination = coins[denom_index]
        
        # notice that for any loop, we must define an end case
        # in this case, we only want to subtract from our 'cents' if the amount we are subtracting (the value of our coin) 
        # is less than or equal to the amount of cents that we have. (in other words, we can't count more money than we have)
        while cents >= denomination:
            cents -= denomination
            coin_count[denom_index] += 1
        # -------------------------------------------
        # MAIN_CODE_END
        # -------------------------------------------
        
        # this is for learning and visualization purposes -- we can delete this line
        print(denomination, ":", coin_count[denom_index])
    
    
    
    # for testing purposes, we want to verify our code is correct:
    # -------------------------------------------
    # TEST_START
    # -------------------------------------------
    
    sum = 0;
    # first we count our results
    for coin_index in range(len(coin_count)):
        denomination = coins[coin_index] # for semantic programming
        count = coin_count[coin_index] # for semantic programming
        sum += denomination * count # see, using semantic programming, isn't this line easy to read?
    
    # now we verify that our code worked correctly
    # print statements are optional -- I always prefer to raise an exception instead (like the example below)
    print("sum: ", sum)
    print("verified? ", sum == temp_cents)
    
    # note that instead of printing the result, we can simply raise an exception like so:
    # in this way, no response means the function worked correctly, 
    # and if it ever doesn't work properly (like if we missed a bug in our logic) then our code will tell us
    
    # but note that sometimes we make a mistake in our logic, (like using an equation that always evaluates to false)
    # so we can start with print statements to visually confirm that our verification logic is correct 
    # before refactoring it into something like this.
    if (sum != temp_cents):
        raise Exception('an error occurred when verifying the results of the function -- cents=(' + str(temp_cents) + ') sum=(' + str(sum) + ")")
    
    # -------------------------------------------
    # TEST_END
    # -------------------------------------------
    
    
    
    # and finally, we can return the result of our function
    # -------------------------------------------
    # RETURN_FUNCTION_RESULTS
    # -------------------------------------------
    return coin_count
    
    
# -------------------------------------------
# call our function
# -------------------------------------------
num_coins_dp(123)