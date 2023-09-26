##testing out HW 1 dimaond problem
s = input("Before you go,I would now like to draw a diamond for you.  Please enter a symbol you would like to use: ")

print("    " + s + "     |")
print("   " + s + s + s + "    |")
print("  "+s + s + s + s + s + "   |")
print(" "+ s + s + s + s + s + s + s + "  |")
print("  "+ s + s + s + s + s + "   |")
print("   " + s + s + s + "    |")
print("    "+ s + "     |")
## trying it out a new way
print("    " + s , end = "     |",)
print("   " + s + s + s , end = "    |")

n = "  "
##ya no that would not work, since the amount of spaces are different and its in the border