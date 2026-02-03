# =========== Python list Methods  ===========
# There are many useful built-in list methods available for you to use.
# Some other list methods can be found below:
#   extend()    - Adds all elements of a list to the another list
#   insert()    - Inserts an item at the defined index
#   remove()    - Removes an item from the list
#   pop()       - Removes and returns an element at the given index
#   index()     - Returns the index of the first matched item
#   count()     - Returns the count of number of items passed as an argument
#   sort()      - Sorts items in a list in ascending order
#   reverse()   - Reverses the order of items in the list

# =========== The Copy Module  ===========
# Let's take a closer look at the copy module.
# There are several ways to make a copy of a list.
# The simplest way to make a copy is to use the copy() method.
# Using the copy() method ensures that if you modify the copied list, the original list remains the same.
# However, if your list contains other lists as items, those inner lists in the original list can still be modified
# if the corresponding inner list in the copied list is modified.
# This is called a shallow copy.
# Slicing lists also creates a shallow copy of a list.
# Therefore, when the list contains other lists as items, the inner lists have to be copied as well.
# You could do this manually but Python already contains a method to do it, the deepcopy() method.
# In order to use the deepcopy() and copy() methods you must import the copy module.

# ************ Example 1 ************
print("Example 1:")
import copy

a = [[1, 2, 3], [4, 5, 6]]
b = copy.copy(a)
c = a[:] #also makes a copy of a
d = copy.deepcopy(a)

b[1][0] = 10
c[1][1] = 11
d[1][2] = 12

print("List a:")
print(a)
print("List b:")
print(b)
print("List c:")
print(c)
print("List d:")
print(d) # Notice how the only change to d is element [1][2] because it's a deep copy

# =========== List Comprehension  ===========
# List comprehension can be used to construct lists in an elegant and concise way.
# This is a powerful tool that will apply some operation to every element in a list, and then put the element into a new list.
# List comprehension consists of an expression followed by a for statement inside square brackets.

# ************ Example 2 ************
print("\nExample 2:")

num_list = ['1', '5', '8', '14', '25', '31']
print(num_list)

new_num_list_ints = [int(element) for element in num_list]
# We are looping over num_list, which is a list of strings 
# For each element, we are casting it to an Integer and putting it into a new list, new_num_list_ints.

print(new_num_list_ints)  # Do you see the difference?

# We can now sum this list, since new_num_list_ints is a list of integers and not strings.
print(sum(new_num_list_ints))
# We can compute the sum of the Integers using the built-in function sum()
# This function gives you 1+5+8+14+25+31=84.

# ************ Example 3 ************
# You can do many operations with list comprehensions. 
print("\nExample 3:")

double_list = [2 * element for element in new_num_list_ints]
# A new list, with each element double its value in the previous list.
print(double_list)

half_list = [0.5 * element for element in new_num_list_ints]
# A new list, with each element half its value from the previous list.
print(half_list)

# =========== Dictionaries ===========

# =========== Creating a Dictionary ===========
# To create a dictionary simply place the items inside curly braces and separate them by commas.
# An item has a key and a value, which is expressed as a pair (key: value)
# Items in a dictionary can have a value of any datatype, however the key must be either a String or number and must be unique.

# ************ Example 4 ************

# An empty dictionary 
empty_dict = {}

# A dictionary with integer keys
int_key_dict = {1: 'apple',
                2: 'banana',
                3: 'orange'
               }

# A dictionary with string keys
string_key_dict = {'name': 'John',
                   'surname': 'Doe',
                   'gender': 'male'
                  }

# A dictionary with mixed keys 
mix_key_dict = {'word': 'Python',
                2: [1, 3, 4, 5]
               }
               
# =========== Accessing Elements from a Dictionary ===========
# While you might use indexing to access elements in a list, dictionaries use keys.
# Keys can be used to access values either by placing them inside square brackets [], such as with indices in lists, or with the get() method.
# Note, if you use the get() method, it will return 'None' instead of 'KeyError', if the key is not found.

# ************ Example 5 ************
print("\nExample 5:")

profile_dict = {'name': 'Chris',
                'surname': 'Smith',
                'age': 28,
                'cell': '083 233 3242'
               }

# Using square brackets []
print(profile_dict['surname'])
# prints out 'Smith'

# Using the get() method
print(profile_dict.get('cell'))
# prints out '083 233 3242'

# =========== Changing Elements in a Dictionary ===========
# We can add new items or change items using the assignment operator (=)
# If there is already a key present, the value gets updated, else if there is no key, a new key: value pair is added.

# ************ Example 6 ************
print("\nExample 6:")

profile_dict = {'name': 'Chris',
                'surname': 'Smith',
                'age': 28,
                'cell': '083 233 3242'
               }

# Changing a value
profile_dict['age'] = 29
print(profile_dict)

# Adding a value
profile_dict['gender'] = 'male'
print(profile_dict)

# =========== Dictionary Membership Test ===========
# You can test if a key is in a dictionary by using the keyword 'in'.
# You simply enter the key you want to test for membership, followed by the 'in' keyword and lastly the name of the dictionary.
# This will return either True or False, depending on whether the dictionary contains the key or not.
# The membership test is for keys only, not for values.

# ************ Example 7 ************
print("Example 7:")

doubles = { 1: 2,
            2: 4,
            3: 6,
            4: 8,
            5: 10
          }

print(1 in doubles)
# prints out True because 1 is a key

print(8 in doubles)
# prints out False because 8 is not a key but a value

# ****************** END OF EXAMPLE CODE ********************* # 

