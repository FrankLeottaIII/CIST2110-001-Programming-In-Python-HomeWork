# HW5.py
# Author: Frank R. Leotta III

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list
FavoriteFoods = ["sushi", "pizza", "steak", "chicken", "pasta"]
print(FavoriteFoods)
# Question 2: Using the list from question 1, print the first and last element of the list
print(FavoriteFoods[0], FavoriteFoods[-1])
# Question 3: Using the list from question 1, print the 3rd element of the list
print ("question 3")
print(FavoriteFoods[2])
# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing
print ("question 4")
print(FavoriteFoods[0:3]) #prints 0,1,2
# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing
print ("question 5")
print(FavoriteFoods[-2:]) #prints -2,-1
# Question 6: Using the list from question 1, create a for each loop that prints each element of the list
print ("question 6")
for x in FavoriteFoods:
    print(x)
# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order
print ("question 7")
for x in reversed(FavoriteFoods):
    print(x)
# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)
print ("question 8")
for i, x in enumerate(FavoriteFoods):
    print(i, x)
# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
list = [[1,2,3],[4,5,6],[7,8,9]]
print ("question 9")
print(list[1][0])

# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list
print ("question 10")
def reverseList(list):
    return list[::-1]

