#1a Write a Python program that prints numbers from 1 to 50, but skips multiples of 5 using the continue statement.
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)
    
#1b Write a Python program to generate the first N Fibonacci numbers using both recursion and iteration. Compare their time complexity
#Using Recursion:
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

N = int(input("Enter N: "))
for i in range(N):
    print(fib(i))
    
#1 Write a Python program using Pandas to perform the following operations using the Titanic dataset:
#Dataset link : titanic.csv
#i. Read the Titanic dataset from a CSV file (titanic.csv) into a Pandas DataFrame and display the first few rows.

import pandas as pd
df = pd.read_csv("titanic.csv")
#print("First few rows of the dataset:")
df.head()

#ii. Filter the dataset to select only the rows where the passenger's age is greater than 30, and display the filtered results.

df[df["Age"] > 30]