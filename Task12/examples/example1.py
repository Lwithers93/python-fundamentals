# ============= Creating a List ==================
# To create a list simply put different comma-separated values between square brackets.

# ************ Example 1 ************
# A List of Strings

string_list = ['John', 'Mary', 'Harry']
# Python knows that anything defined in [] is a list.
# There are 3 string items in this list.

# ************ Example 2 ************
# A list containing different datatypes

mixed_list = ['Hello', 3.4, 89, 'World']

# ************ Example 3 ************
# A list containing another list

my_list = ['Monkey', 'Elephant', [3, 4, 6, 10]]

# ============= Indexing Lists ==================
# We are able to access all elements in a list using the index operator [].
# The index starts from 0 for the leftmost item, so a list having 10 elements will have indices from 0 to 9.
# Alternatively the index can begin with -1 for the index of the rightmost item, so a list having
# 10 elements will have indices from -10 to -1.

# ************ Example 4 ************
print("Example 4: ")

pet_list = ['cat', 'dog', 'hamster', 'goldfish', 'parrot']

print(pet_list[0])
# Prints 'cat'.
# The element at position 0 is also known as the first element of a list, or the 'element at index 0'.

print(pet_list[-2])
# Prints 'goldfish'
# The element at position -2 is also known as the 4th element of the list, or the 'element at index -2'. 

# ============= Slicing Lists ==================
# You can slice lists in the same way as you would slice strings.
# We can access a range of items in a list by using the slicing operator (colon).
# In order to slice a list you need to indicate a start and end position of the items you would like to access.
# You place these positions between the square brackets of the index operator [] and separate them with the colon.
# The item in the start position is included in the sliced list, while the item in the end position is not included.

# ************ Example 5 ************
print("\nExample 5: ")

num_list = [1, 4, 2, 7, 5, 9]

print(num_list[1:2])
# Prints from position 1 up to position 2, but does NOT include the element at position 2,
# so it only prints the item in position 1, i.e. 4.

print(num_list[0:])
# Prints everything from the 0th position to the end of the list i.e. the entire list.

print(num_list)
# A faster way to print the entire list. 

# ============= Changing Elements in a Lists ==================
# Elements in a list can be changed.
# You use the assignment operator (=) to change single or multiple elements.

# ************ Example 6 ************
print("\nExample 6:")

name_list = ['James', 'Molly', 'Chris', 'Peter', 'Kim']
name_list[2] = 'Tom'
# We can replace the 3rd element of the list with a new string.
# 'Chris' will be lost and replaced with 'Tom'. 
print(name_list) # To see that the list has changed.

name_list[1:4] = ['Joe', 'Lucy', 'Kelly']
# Here we replace the 2nd, 3rd and 4th elements of the list with a new string.
print(name_list) # To see that the list has changed.

# ============= Adding Elements to a Lists ==================
# You can add an element to the end of a List using the 'append()' method.

# ************ Example 7 ************
print("\nExample 7:")

new_list = [34, 35, 75, 'Coffee', 98.8]
new_list.append('Tea')
# Adds the String 'Tea' to the end of the list
print(new_list)

# ============= Deleting Elements From a list ==================
# You can use the 'del' keyword to delete one or more items from a list.
# You are even able to delete the list entirely.

# ************ Example 8 ************
print("\nExample 8:")

char_list = ['P', 'y', 't', 'h', 'o', 'n']

del char_list[3]
# Deletes the single element 'h'
print(char_list)

del char_list[1:3]
# Deletes multiple elements from the 2nd to 4th element.
print(char_list)

del char_list
# Deletes the entire list

# ============= Getting the Length of a List ==================
# You can get the length of the list (how many elements there are in the list) by using the len() function.
# This is the same function we used to get the length of a string. 

# ************ Example 9 ************
print("\nExample 9:")

oddNum_list = [1, 3, 5, 7, 9]
print(len(oddNum_list))
# Will print the total number of items in the list, currently 5.

# ================== Looping Over Lists ==================
# What if you have a list of items and you want to do something to each item?
# You simply use a for loop to loop over every item in the list.

# ************ Example 10 ************
print("\nExample 10:")

food_list = ['Pizza', 'Burger', 'Fries', 'Pasta', 'Salad'] #Define a list of strings

for food in food_list:
    print(food)
# This loop prints out every item in the list. 
# This is a very powerful tool in Python and shows how you can simply loop through a list.

# ************ Example 11 ************
print("\nExample 11:")
numbers = [1,2,3,4]

for num in numbers:
    print(num)
# Any type of list can be looped over using this construct.
# The above will print out the numbers 1 to 4 - i.e. the entries in list 'numbers'.

# ================== Checking if Something is in a List ==================
# You can simply use an if statement to check if a certain item is in a list.

# ************ Example 12 ************
print("\nExample 12:")
grocery_list = ['Bread', 'Milk', 'Butter', 'Cheese', 'Cereal']

if 'Apples' in grocery_list:
    print('The item Apples was found in the list grocery_list')
else:
    print('The item Apples was not found in the list grocery_list')
        
# This is a much quicker way than looping through all the items, such as if you did:
for item in grocery_list:
    if item == 'Apples':
        print('The item Apples was found in the list grocery_list')

# ================== Using the range Function ==================
# The range function is a special Python function, that will automatically generate a list of integers within a specified range.

# ************ Example 13 ************
print("\nExample 13:")

num_til_10 = list(range(0,10))
print(num_til_10)
# This will create a list of integers =[0,1,2,3,4,5,6,7,9] and store it in the variable 'num_til_10'.

num_til_5 = list(range(0,5)) 
# This will create a list of integers =[0,1,2,3,4] and store it in the variable 'num_til_5'.

num_2_til_5 = list(range(2,5))
# This will create a list of integers =[2,3,4] and store it in the variable 'num_2_til_5'.

# The resulting list can be looped over like any list of integers, e.g., to print the numbers from 1 to 10:
for num in num_til_10:
    print(num)

print("\n")

# Since num_til_10 = list(range(0,10)), the above for loop is exactly the same as:
for num in list(range(0,10)):
    print(num)

# ****************** END OF EXAMPLE CODE ********************* # 


