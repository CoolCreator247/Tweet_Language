def lexer():
     
    tweet_input = ""
    
    # Math
    result = tweet_input.find("+")
    Adding = True

    result = tweet_input.find("-")
    Subtraction = True

    result = tweet_input.find("/")
    Division = True

    result = tweet_input.find("x")
    Times = True

    #Vars
    result = tweet_input.find("var =")
    vars 