## exiting the program
import time
walrus = True
end = None
end = bool(end)
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
        return walrus == True
    else:
        print("error, looks like you will have to play it again\n")
        return walrus == False

while walrus == True:
    restart_or_quit(walrus)
        
 

"""
while walrus < 10:
    print(walrus)
    walrus += 1
    if walrus == 6:
        break
    """