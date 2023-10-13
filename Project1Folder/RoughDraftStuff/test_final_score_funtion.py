

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
    elif SCORE == 0:
        return print("Better luck next time!\nThank you for playing!")
    else:
        return print("Hmm, something went wrong with the score, please contact the developer") 


final_score()

##StopAsyncIteration = False pop up in copilot... ill  have to look into that

"""###mistakes I made, remember to not do this again###
print("testing below")

print(final_score(SCORE))
that prints out final score flavor text, 
            but also prints out none
because I was calling the function incorrectly


"""

""" Old text###
## This is a test for final score funtion
## it keeps giving me a non after it , which I do not need
## I need to fix it
"""

### ok now for the main

def main():
    main()


##interesting copilot stuff
###  I guess I should add a path: to the top of each file
# Compare this snippet from Project1Folder/Project1_v0.05.py:
#     option_4 = "d"
# Path: Project1Folder/Project1_v0.06.py
if __name__ == "__main__":
    final_score()
