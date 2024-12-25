PROGRAM 1  data type 
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

# Create a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Insert an element at a specific index
my_list.insert(2, 10)
print("List after inserting 10 at index 2:", my_list)

# Remove an element from the list
my_list.remove(5)
print("List after removing 5:", my_list)

# Append an element to the end of the list
my_list.append(20)
print("List after appending 20:", my_list)

# Get the length of the list
list_length = len(my_list)
print("Length of the list:", list_length)

# Remove the last element from the list
last_element = my_list.pop()
print("Last element removed from the list:", last_element)
print("List after removing the last element:", my_list)

# Clear all elements from the list
my_list.clear()
print("List after clearing all elements:", my_list)










===========================================================================================================================================================================================

PROGRAM 3

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# Get the length of the tuple
tuple_length = len(my_tuple)
print("Length of the Tuple:", tuple_length)

# Check if an item exists in the tuple
check = 2 in my_tuple
print("Is 2 in the Tuple?:", check)

# Access items in the tuple
print("Item at index 2:", my_tuple[2])

# Convert the tuple to a list as tuples are immutable
my_list = list(my_tuple)

# Insert an element at a specific index in the list
my_list.insert(2, 20)

# Append an element to the end of the list
my_list.append(6)

# Convert the list back to a tuple
my_tuple = tuple(my_list)

# Print the updated tuple
print("Updated Tuple:", my_tuple)










=========================================================================================================================================================================================




PROGRAM 4


# Create a dictionary
student = {"name": "Mary", "age": 20, "grade": "A"}

# Print the dictionary items directly
print("Dictionary items using items():")
print(student.items())

# Print the dictionary items by traversing it
print("\nDictionary items by traversing:")
for key, value in student.items():
    print(f"{key}: {value}")

# Access items in the dictionary using keys
print("\nAge of student:", student["age"])

# Use the get() method to access items
print("Grade of student:", student.get("grade"))

# Change values in the dictionary
student["grade"] = "B"
print("\nUpdated dictionary:", student)

# Get the length of the dictionary
dict_length = len(student)
print("Length of the dictionary:", dict_length)













===============================================================================================================================================================================





PROGRAM 5


# Define functions for operations
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

# Create menu
while True:
    print("\nARITHMETIC OPERATIONS")
    print("1. TO PERFORM ADDITION")
    print("2. TO PERFORM SUBTRACTION")
    print("3. TO PERFORM MULTIPLICATION")
    print("4. TO PERFORM DIVISION")
    print("5. EXIT")

    # Get user choice
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    # Exit condition
    if choice == 5:
        print("Exiting the program.")
        break

    # Get numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    # Perform operation based on choice
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



# Input a number
num = int(input("Enter a number: "))

# Check if the number is positive or negative
if num >= 0:
    print(num, "is a positive number")
else:
    print(num, "is a negative number")






=================================================================================================================================================================================



PROGRAM 7


# Input list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a function to check for even numbers
def is_even(num):
    return num % 2 == 0

# Use filter() to filter only even numbers
even_numbers = list(filter(is_even, numbers))

# Print the filtered list of even numbers
print("The even numbers are:", even_numbers)






=========================================================================================================================================================================================

PROGRAM 8

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print the date and time
print("Today's date and time:", now)




============================================================================================================================================================================================


PROGRAM 9

import datetime

# Get the current date
today = datetime.datetime.now().date()

# Print the current date
print("Current Date is:", today)

# Input number of days to add
days_to_add = int(input("Enter the number of days to add: "))

# Add the days to the current date
new_date = today + datetime.timedelta(days=days_to_add)

# Print the new date
print("Date after adding", days_to_add, "days is:", new_date)








===================================================================================================================================================================================================





PROGRAM 10


def count_characters(string):
    # Create an empty dictionary
    char_count = {}

    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count by 1
        if char in char_count:
            char_count[char] += 1
        else:
            # If the character is not in the dictionary, add it and set its count to 1
            char_count[char] = 1

    # Return the dictionary
    return char_count

# Input the string
string = input("Enter a string: ")

# Call the function and store the result in a variable
result = count_characters(string)

# Print the result
print(f"Character count in '{string}' is: {result}")









=====================================================================================================================================================================================================


PROGRAM 11


def count_characters(filename):
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the contents of the file into a string
        contents = file.read()

    # Create an empty dictionary
    char_count = {}

    # Loop through each character in the string
    for char in contents:
        # If the character is already in the dictionary, increment its count by 1
        if char in char_count:
            char_count[char] += 1
        else:
            # If the character is not in the dictionary, add it and set its count to 1
            char_count[char] = 1

    # Return the dictionary
    return char_count

# Input the data
data = input("Enter the data: ")

# Input the filename to save the data
filename = input("Enter the filename to save the data: ")

# Write the data to the file
with open(filename, "w") as file:
    file.write(data)

# Output that the file is being opened for reading
print(f"Opening the file '{filename}' for reading...")

# Call the function to count the frequency of characters in the file
char_count = count_characters(filename)

# Print the result
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

#Create a one-dimensional array

arr np.array([1, 2, 3, 4, 5])

#Print the type of the array print("Type of array:", type(arr))

#Print the number of axes of the array print("Axes of array:", np.ndim(arr))

Output:

Type of array: <class 'numpy.ndarray'>

Axes of array: 1

Shape of array: (5,)

Type of elements in array: int32

#Print the shape of the array print("Shape of array:", arr.shape)

#Print the type of elements in the array print("Type of elements in array:", arr.dtype)











=======================================================================================================================================================================================================\\\\\\








PROGRAM 13


Program 13: Write a python program to concatenate the dataframes with two different objects.

import pandas as pd

#Create a first DataFrame df1

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

#Read the csv file into a DataFrame using pd.read_csv()

df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")

#Display the first 5 rows of the DataFrame using head()

print("First 5 Rows:")

print(df.head(5))

# Display the last 5 rows of the DataFrame using tail()

print("\nLast 5 Rows:")

print(df.tail(5))




==============================================================================================================================================================================================================







PROGRAM 15

import math

# Get the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius**2

# Print the result
print("The area of the circle is", area)




==========================================================================================================================================================================================================




16 A


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame using pd.read_csv()
df = pd.read_csv("salesData.csv")

# Get the data for the "Total Profit" column
total_profit = df["Total Profit"]

# Plot the total profit data
plt.plot(total_profit, color='blue', marker='o', linestyle=':', label="Total Profit", linewidth=4)

# Add X and Y axis labels
plt.xlabel("Months")
plt.ylabel("Total Profit")

# Add title
plt.title("Profit Trend of All Products")

# Add a legend at the lower right location
plt.legend(loc="lower right")

# Add xticks to include all months
plt.xticks(range(len(df)), df['Months'], rotation=45)

# Show the plot
plt.show()











==================================================================================================================================================================================================

16 B

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame using pd.read_csv()
df = pd.read_csv("salesData.csv")

# Plot the units sold data for each product with different line colors
plt.plot(df["Months"], df['Pen'], color='blue', marker='o', label="Pen")
plt.plot(df["Months"], df['Book'], color='red', marker='o', label="Book")
plt.plot(df["Months"], df['Marker'], color='green', marker='o', label="Marker")
plt.plot(df["Months"], df['Chair'], color='yellow', marker='o', label="Chair")
plt.plot(df["Months"], df['Table'], color='purple', marker='o', label="Table")
plt.plot(df["Months"], df['Pen Stand'], color='orange', marker='o', label="Pen Stand")

# Add X and Y axis labels
plt.xlabel("Months")
plt.ylabel("Sold Units")

# Add title
plt.title("Sales Trend By Product")

# Add a legend at the upper left location
plt.legend(loc="upper left")

# Show the plot
plt.show()










======================================================================================================================================================================================




16 C



import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame using pd.read_csv()
df = pd.read_csv("salesData.csv")

# Extract the data for Chair and Table products
data = df[["Months", "Chair", "Table"]]

# Create a bar chart for Chair and Table products with bar width = 0.35
bar_width = 0.35
index = range(len(data))  # Index for the x-axis

# Create bars for Chair and Table
chair_bar = plt.bar(index, data['Chair'], bar_width, color='blue', label='Chair')
table_bar = plt.bar([i + bar_width for i in index], data['Table'], bar_width, color='red', label='Table')

# Add X and Y axis labels
plt.xlabel("Months")
plt.ylabel("Sold Units")

# Add title
plt.title("Sales Trend of Chair and Table")

# Add a legend at the upper right location
plt.legend(loc="upper left")

# Set the X-axis tick labels to be the months
plt.xticks([i + bar_width / 2 for i in index], data['Months'], rotation=45)

# Show the plot
plt.show()












































16 D


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame using pd.read_csv()
df = pd.read_csv("salesData.csv")

# Extract the data for all products
data = df[["Months", "Pen", "Book", "Marker", "Chair", "Table", "Pen Stand"]]

# Plot the data using stackplot
plt.stackplot(data["Months"], data["Pen"], data["Book"], data["Marker"], data["Chair"], data["Table"], data["Pen Stand"], 
              labels=["Pen", "Book", "Marker", "Chair", "Table", "Pen Stand"])

# Add X and Y axis labels
plt.xlabel("Months")
plt.ylabel("Sold Units")

# Add a legend at the upper left location
plt.legend(loc="upper left")

# Add title
plt.title("Sales Trend of All Products")

# Show the plot
plt.show()

