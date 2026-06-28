"""Q6. (Sets + Tuples + Modules)
Write a program that:
Takes 10 numbers as input and stores unique numbers in a set.
Converts that set into a tuple.
Uses random module to pick and print 3 random numbers from the tuple.
Uses math module to print the square root of the sum of the tuple elements.
Handle possible exceptions."""


import random as r
from math import sqrt as sr


num = set()


try:
    while len(num) <10:
        num.add(int(input("Enter the number:")))
except ValueError as v:
    print(v)
    
print(f"10 Unique numbers given by user are:{num}")


print("Converting set into tuple:")
print(f"Before conversion type is:{type(num)}")

num =tuple(num)

print(f"After conversion type is:{type(num)}")

print(f"Three Random numbers from tuple:{num} are:")

for i in range(3):
    print(r.choice(num))

try:
    sum = 0
    print("Square root of the sum of the tuple elements are:")
    for i in num:
        sum +=i
    print(sr(sum))
except Exception as e:
    print(e)