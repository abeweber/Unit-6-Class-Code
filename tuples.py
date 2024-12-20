"""
Name: Abe Weber
Date: 12/16/24
"""

# the look like an ordered pair in math

# make tuple with two items
my_tuple = ("3",4)
print(my_tuple)
# make tuple with one item
lonely_tuple = (5,)
print(lonely_tuple)

# You access elements from them using [] just like strings
print(my_tuple[0])

# also like strings, you can only concatenate tuples with other tuples
not_lonely_tuple = my_tuple + (5,)
print(not_lonely_tuple)

character_info = (("Rosalie",100),("Cedric", 75), ("Shana",94))
print(character_info[1][0])