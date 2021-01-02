#Tuple

#1
#Create a Tuple
# Set the tuples
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekend = "Saturday", "Sunday"
# Print the tuples
print('-------------------------EX1---------------------------------')
print(weekdays)
print(weekend)

#2
#Single Item Tuples
a = ("Cat")
b = ("Cat",)
print('-------------------------EX2---------------------------------')
print(type(a))
print(type(b))

#3
#Tuple containing a List
# Set the tuple
t = ("Banana", ['Milk', 'Choc', 'Strawberry']) 
print('-------------------------EX3---------------------------------')
# Print the tuple
print(t)

#4
#Access the Values in a Tuple
# Set the tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print('-------------------------EX4---------------------------------')
# Print the second element of the tuple
print(weekdays[1])

#range
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(weekdays[1:4])

#5
#Access a List Item within a Tuple
t = (101, 202, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]) 
print('-------------------------EX5---------------------------------')
print(t[2][1])

#6
#Update a Tuple
# Set and print the initial tuple
weekend = ("Saturday", "Sunday")
print('-------------------------EX6---------------------------------')
print(weekend)
# Reassign and print
weekend = ("Sat", "Sun")
print(weekend)

#7
#Update a List Item within a Tuple
# Assign the tuple
t = (101, 202, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]) 
print('-------------------------EX7---------------------------------')
print(t)
# Update the third list item
t[2][2] = "Humpday"
print(t)

#8
#Concatenate Tuples (Combine)
#Can also use a tuple as the basis for another tuple. 
#For example, can concatenate a tuple with another one to create a new a tuple that contains values from both tuples.
# Set two tuples
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekend = ("Saturday", "Sunday")
# Set a third tuple to the value of the previous two
alldays = weekdays + weekend
print('-------------------------EX8---------------------------------')
# Print them all
print(weekdays)
print(weekend)
print(alldays)

#9
#Delete a Tuple
t = (1,2,3)
del t

#10
#Named Tuples
#Need to import modules
# Import the 'namedtuple' function from the 'collections' module
from collections import namedtuple
# Set the tuple
individual = namedtuple("Individual", "name age height")
user = individual(name="R3in3", age=20, height=160)
print('-------------------------EX10---------------------------------')
# Print the tuple
print(user)
# Print each item in the tuple
print(user.name)
print(user.age)
print(user.height)
print('-------------------------THANK YOU---------------------------------')
