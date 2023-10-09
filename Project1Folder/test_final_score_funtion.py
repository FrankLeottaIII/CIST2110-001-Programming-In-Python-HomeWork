## This is a test for final score funtion
## it keeps giving me a non after it , which I do not need
## I need to fix it

SCORE = 0
def final_score()-> str:
    global SCORE
    print("Your final score is " + str(SCORE) + " out of 5")
    if SCORE == 5:
       return print("one hundred percent! Perfect score!")
    elif SCORE == 4:
        return print("80 percent Great job!")
    elif SCORE == 3:
        return print("you passed, but just by the skin of your teeth!")
    elif SCORE == 2:
        return print("Not bad!")
    elif SCORE == 1:
        return print("You can do better!")
    else:
        return print("Better luck next time!\nThank you for playing!") 


final_score()

##StopAsyncIteration = False pop up in copilot... ill  have to look into that

"""###mistakes I made, remember to not do this again###
print("testing below")

print(final_score(SCORE))
that prints out final score flavor text, 
            but also prints out none
because I was calling the function incorrectly


"""