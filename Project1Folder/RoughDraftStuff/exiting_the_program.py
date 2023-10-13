## exiting the program
walrus = True


#how do I would you like to play again with a while loop?
#how do I would you like to play again with a while loop?
def restart_or_quit()-> bool:
    global play_or_quit
    play_or_quit = input("Would you like to play again? Y for YES and N for NO :   ")
    while play_or_quit != "y" and play_or_quit != "n" and play_or_quit != "Y" and play_or_quit != "N" and play_or_quit != "test":
        print("I think you mistyped, please try again.\n")
        play_or_quit = input("Would you like to play again? Y for YES and N for NO :  ")
    if play_or_quit == "y" or play_or_quit == "Y":
        return play_or_quit == False
    if play_or_quit == "n" or play_or_quit == "N":
        return play_or_quit == True
    if play_or_quit == "test":
        restart_or_quit()
    else:
        print("error please answer that again")
        restart_or_quit()
#
while walrus == True:
    end = restart_or_quit()
    if end == False:
      exit()
    if end == True:
        print("test")
        walrus = False
        end = restart_or_quit()

###I am so tired... I am 

""""""
walrus = False
while walrus == False:
    Score = 0
    welcome()
    time.sleep(1)
    q1 = ask_question("1.) Which tree is part of the red oak subspecies?", "A. white oak", "B. black oak", "C. red maple", "D. chestnut oak", "B")
    score_now(q1, SCORE)
    time.sleep(1)
    q2 = ask_question("2.) Which tree is part of the white oak subspecies?", "A. post oak", "B. scarlet oak", "C. silver maple", "D. willow oak", "A")
    score_now(q2, SCORE)
    time.sleep(1)
    q3 = ask_question("3.) In ecological silviculture, what is NOT true about the selection system?", "A. it is a silvicultural system that maintains uneven aged stands.", "B. Often represented by “reverse J” dia. distrib. or something slightly more irregular", "C. It is a silvicultural system that maintains even aged stands.", "D. It is a silvicultural system that includes 3 or more age classes of trees.", "C")
    score_now(q3, SCORE)
    time.sleep(1)
    q4 = ask_question("4.) what is NOT true about the B-D-q method?", "A.  it provides a guiding curve approach", "B.  applies to group selection", "C.  applies to single tree selection", "D.  it uses a ratio of small tree to large trees in its calculations", "B")
    score_now(q4, SCORE)
    time.sleep(1)
    q5 = ask_question("5.) What does the D stand for in the B-D-q method?", "A.  diameter", "B.  Largest density class in the residual stand", "C.  Largest diameter class in the residual stand", "D.  diameter ratio", "C")
    score_now(q5, SCORE)
    time.sleep(1)
    final_score()
    time.sleep(1)
    walter = restart_or_quit(walter)
    if walter == True:
        walrus = False
    if walter == False:
        exit()




""""""

""" CODE THAT WORKS
play_or_quit = input("Would you like to play again? Y for YES and N for NO:  ")
while play_or_quit != "y" and play_or_quit != "n" and play_or_quit != "Y" and play_or_quit != "N" and play_or_quit != "test":
    print("I think you mistyped, please try again.\n")
    play_or_quit = input("Would you like to play again? Y for YES and N for NO\n Your answer: ")   
    if play_or_quit == "y" or play_or_quit == "Y":
        continue
    if play_or_quit == "n" or play_or_quit == "N":
        exit() 
"""


###... It was the \n in the print statement that was messing it up
### it is 1:14 am and I am tired, but I am glad I figured it out



"""while walrus == True:
    play= input("Would you like to play again? Y for YES and N for NO\n Your answer: ")
    while play != "y" and play != "n" and play != "Y" and play != "N":
        print("I think you mistyped, please try again.\n")
        play = input("Would you like to play again? Y for YES and N for NO) ")    
    if play == "y" or play == "Y":
        walrus = False
        
    if play == "n" or play == "N":
        walrus = True
    else:
        print("error, looks like you will have to play it again\n")
        walrus = False
        break

"""
"""
def restart_or_quit(varible)-> bool:
    global walrus
    play_or_quit = input("Would you like to play again? Y for YES and N for NO\n Your answer: ")
    while play_or_quit != "y" and play_or_quit != "n" and play_or_quit != "Y" and play_or_quit != "N":
        print("I think you mistyped, please try again.\n")
        play_or_quit = input("Would you like to play again? Y for YES and N for NO) ")
    if play_or_quit == "y" or play_or_quit == "Y":
        return varible == False
    if play_or_quit == "n" or play_or_quit == "N":
        return varible == True
    else:
        print("error, looks like you will have to play it again\n")
        return varible == False

while walrus == True:
    restart_or_quit(walrus)
    if walrus == False:
        exit()
"""

"""
def restart_or_quit(end: bool)-> bool:
    global play_or_quit
    global walrus
    play_or_quit = input("Would you like to play again? Y for YES and N for NO\n Your answer: ")
    while play_or_quit != "y" and play_or_quit != "n" and play_or_quit != "Y" and play_or_quit != "N":
        print("I think you mistyped, please try again.\n")
        play_or_quit = input("Would you like to play again? Y for YES and N for NO)")
    if play_or_quit == "y" or play_or_quit == "Y":
        return end == False
    if play_or_quit == "n" or play_or_quit == "N":
        return end == True
    else:
        print("error, looks like you will have to play it again\n")
        return end == False

while walrus == True:
    restart_or_quit(walrus)
    if end == True:
        walrus = False
        break
    if end == False:
        walrus = True
if walrus == False:
    exit()        
"""        
 ###this isnt working, and its getting late. just going to use an exit() for now.

"""
while walrus < 10:
    print(walrus)
    walrus += 1
    if walrus == 6:
        break
    """