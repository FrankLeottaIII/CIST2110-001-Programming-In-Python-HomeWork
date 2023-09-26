##testing out HW 1 dimaond problem
s = input("Before you go,I would now like to draw a diamond for you.  Please enter a symbol you would like to use: ")

print("    " + s + "     |")
print("   " + s + s + s + "    |")
print("  "+s + s + s + s + s + "   |")
print(" "+ s + s + s + s + s + s + s + "  |")
print("  "+ s + s + s + s + s + "   |")
print("   " + s + s + s + "    |")
print("    "+ s + "     |")
print(" ")
## trying it out a new way
print("    " + s , end = "     |\n")
print("   " + s + s + s , end = "    |\n")

n = "  "
##looks more professional this wa, but still a hasle if I have to put end =  each line... but it works