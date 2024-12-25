PROGRAM 1  
a = 10
print("Type of a:", type(a))
print("Value of a:", a)

b = 20.5
print("Type of b:", type(b))
print("Value of b:", b)

c = "Python"
print("Type of c:", type(c))
print("Value of c:", c)

d = True
print("Type of d:", type(d))
print("Value of d:", d)

e = [1, 2, 3, 4]
print("Type of e:", type(e))
print("Value of e:", e)

f = (1, 2, 3, 4)
print("Type of f:", type(f))
print("Value of f:", f)

g = {1, 2, 3, 4}
print("Type of g:", type(g))
print("Value of g:", g)

h = {"name": "Srikanth", "age": 30}
print("Type of h:", type(h))
print("Value of h:", h)

i = None
print("Type of i:", type(i))
print("Value of i:", i)

PROGRAM 2 

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

my_list.insert(2, 10)
print("List after inserting 10 at index 2:", my_list)

my_list.remove(5)
print("List after removing 5:", my_list)

my_list.append(20)
print("List after appending 20:", my_list)

list_length = len(my_list)
print("Length of the list:", list_length)

last_element = my_list.pop()
print("Last element removed from the list:", last_element)
print("List after removing the last element:", my_list)

my_list.clear()
print("List after clearing all elements:", my_list)


===========================================================================================================================================================================================

PROGRAM 3


my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

tuple_length = len(my_tuple)
print("Length of the Tuple:", tuple_length)

check = 2 in my_tuple
print("Is 2 in the Tuple?:", check)

print("Item at index 2:", my_tuple[2])

my_list = list(my_tuple)

my_list.insert(2, 20)

my_list.append(6)

my_tuple = tuple(my_list)

print("Updated Tuple:", my_tuple)


=========================================================================================================================================================================================


PROGRAM 4

student = {"name": "Mary", "age": 20, "grade": "A"}

print("Dictionary items using items():")
print(student.items())

print("\nDictionary items by traversing:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\nAge of student:", student["age"])

print("Grade of student:", student.get("grade"))

student["grade"] = "B"
print("\nUpdated dictionary:", student)

dict_length = len(student)
print("Length of the dictionary:", dict_length)

===============================================================================================================================================================================


PROGRAM 5


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

while True:
    print("\nARITHMETIC OPERATIONS")
    print("1. TO PERFORM ADDITION")
    print("2. TO PERFORM SUBTRACTION")
    print("3. TO PERFORM MULTIPLICATION")
    print("4. TO PERFORM DIVISION")
    print("5. EXIT")


    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 5:
        print("Exiting the program.")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == 1:
        result = add(num1, num2)
        print("Result:", result)
    elif choice == 2:
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == 4:
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid option, please try again.")

==============================================================================================================================================================================

PROGRAM 6

num = int(input("Enter a number: "))

if num >= 0:
    print(num, "is a positive number")
else:
    print(num, "is a negative number")

=================================================================================================================================================================================



PROGRAM 7

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))

print("The even numbers are:", even_numbers)


=========================================================================================================================================================================================

PROGRAM 8

import datetime

now = datetime.datetime.now()

print("Today's date and time:", now)

============================================================================================================================================================================================


PROGRAM 9

import datetime

today = datetime.datetime.now().date()

print("Current Date is:", today)


days_to_add = int(input("Enter the number of days to add: "))

new_date = today + datetime.timedelta(days=days_to_add)

print("Date after adding", days_to_add, "days is:", new_date)


===================================================================================================================================================================================================





PROGRAM 10


def count_characters(string):
    
    char_count = {}

    for char in string:
    
        if char in char_count:
            char_count[char] += 1
        else:
    
            char_count[char] = 1
        
    return char_count

string = input("Enter a string: ")

result = count_characters(string)

print(f"Character count in '{string}' is: {result}")


=====================================================================================================================================================================================================


PROGRAM 11


def count_characters(filename):
    
    with open(filename, "r") as file:
    
        contents = file.read()

    char_count = {}

    for char in contents:
        
        if char in char_count:
            char_count[char] += 1
        else:
            
            char_count[char] = 1

    return char_count

data = input("Enter the data: ")

filename = input("Enter the filename to save the data: ")

with open(filename, "w") as file:
    file.write(data)

print(f"Opening the file '{filename}' for reading...")

char_count = count_characters(filename)

print(f"Character frequency in '{filename}' is:", char_count)

============================================================================================================================================================================================

PROGRAM 12


Program 12:

Using a numpy module create an array and check the following

1. Type of array

3. Shape of array

2. Axes of array

4. Type of elements in array.

import numpy as np.


arr np.array([1, 2, 3, 4, 5])


Output:

Type of array: <class 'numpy.ndarray'>

Axes of array: 1

Shape of array: (5,)

Type of elements in array: int32


=======================================================================================================================================================================================================\\\\\\


PROGRAM 13


Program 13: Write a python program to concatenate the dataframes with two different objects.

import pandas as pd

df1= pd.DataFrame({'Name': ['Snigdha', 'Smayan', 'Satvik'],

'age': [20,19,18],

'grade': ['A', 'C', 'A']},

index=[1,2,3])

Create a second DataFrame df2

df2 pd.DataFrame({'Name': ['Mary', 'Nirmala', 'Shantala'],

'age': [23,30,28],

'grade': ['B', 'C', 'A']),

index=[4,5,6])

Concatenate the two DataFrames into a single DataFrame

pd.concat([df1, df2]) result

Display the concatenated DataFrame

print(result)

=============================================================================================================================================================================================================\\\


PROGRAM 14

import pandas as pd


df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")

print("First 5 Rows:")

print(df.head(5))

print("\nLast 5 Rows:")

print(df.tail(5))


==============================================================================================================================================================================================================


PROGRAM 15

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius**2

print("The area of the circle is", area)



==========================================================================================================================================================================================================

16 A


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("salesData.csv")

total_profit = df["Total Profit"]

plt.plot(total_profit, color='blue', marker='o', linestyle=':', label="Total Profit", linewidth=4)

plt.xlabel("Months")
plt.ylabel("Total Profit")

plt.title("Profit Trend of All Products")

plt.legend(loc="lower right")

plt.xticks(range(len(df)), df['Months'], rotation=45)

plt.show()


==================================================================================================================================================================================================

16 B

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("salesData.csv")

plt.plot(df["Months"], df['Pen'], color='blue', marker='o', label="Pen")
plt.plot(df["Months"], df['Book'], color='red', marker='o', label="Book")
plt.plot(df["Months"], df['Marker'], color='green', marker='o', label="Marker")
plt.plot(df["Months"], df['Chair'], color='yellow', marker='o', label="Chair")
plt.plot(df["Months"], df['Table'], color='purple', marker='o', label="Table")
plt.plot(df["Months"], df['Pen Stand'], color='orange', marker='o', label="Pen Stand")

plt.xlabel("Months")
plt.ylabel("Sold Units")

plt.title("Sales Trend By Product")

plt.legend(loc="upper left")

plt.show()

======================================================================================================================================================================================

  16 C



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("salesData.csv")

data = df[["Months", "Chair", "Table"]]

bar_width = 0.35
index = range(len(data)) 

chair_bar = plt.bar(index, data['Chair'], bar_width, color='blue', label='Chair')
table_bar = plt.bar([i + bar_width for i in index], data['Table'], bar_width, color='red', label='Table')


plt.xlabel("Months")
plt.ylabel("Sold Units")

plt.title("Sales Trend of Chair and Table")

plt.legend(loc="upper left")

plt.xticks([i + bar_width / 2 for i in index], data['Months'], rotation=45)

plt.show()


16 D


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("salesData.csv")

data = df[["Months", "Pen", "Book", "Marker", "Chair", "Table", "Pen Stand"]]

plt.stackplot(data["Months"], data["Pen"], data["Book"], data["Marker"], data["Chair"], data["Table"], data["Pen Stand"], 
              labels=["Pen", "Book", "Marker", "Chair", "Table", "Pen Stand"])

plt.xlabel("Months")
plt.ylabel("Sold Units")

plt.legend(loc="upper left")

plt.title("Sales Trend of All Products")

plt.show()

