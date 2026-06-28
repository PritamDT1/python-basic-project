"""Q7. (Lambda + range() + Lists + Exception Handling)
Create a lambda function to calculate the square of a number.
Write a program that:
Uses range(1, 21) to generate numbers.
Stores the squares of these numbers in a list using the lambda function.
Prints only the even squares from the list.
Add exception handling if needed."""


print("Q7. (Lambda + range() + Lists + Exception Handling)")

sqr = lambda num: num**2

squres = list()

for i in range(1,21):
    squres.append(sqr(i))
    
print(f"Our list is:{squres}")

print("Printing only Even squres from the list:")

for i in squres:
    if i%2 == 0:
        print(f"->{i}")
        
    else:
        continue
    

    

