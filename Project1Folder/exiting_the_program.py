## exiting the program
walrus = True


#how do I would you like to play again with a while loop?
#how do I would you like to play again with a while loop?
play_or_quit = input("Would you like to play again? Y for YES and N for NO:  ")
while play_or_quit != "y" and play_or_quit != "n" and play_or_quit != "Y" and play_or_quit != "N":
    print("I think you mistyped, please try again.\n")
    play_or_quit = input("Would you like to play again? Y for YES and N for NO\n Your answer: ")   
    if play_or_quit == "y" or play_or_quit == "Y":
        continue
    if play_or_quit == "n" or play_or_quit == "N":
        exit() 


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