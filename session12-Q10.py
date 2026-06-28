"""Q10. (Mini Project - Comprehensive) 
Create a Smart Calculator & Data Manager program that combines multiple concepts: 
Use a while loop menu with these options: 
1. Basic Arithmetic (use functions + exception handling) 
2. Scientific Calculations (use math module) 

3. Generate Random Numbers (use random module) 
4. Store Results in Dictionary (with timestamp using string) 
5. View History (show stored results) 
6. Exit 
"""

print("Q10. (Mini Project - Comprehensive)")

import math as m
import random as r
import time as t

database = dict()
class Cal:
    def __init__(self):
        pass
    
    def basic(self):
    
        try:
            chc= 0
            while chc !=-1:
                print("1.Addition            2.Substraction")
                print("3.Multiplication      4.Division")
                print("5.Modulas            -1.Exit")
                chc= int(input("Enter the choice:"))
                if chc ==-1:
                    break
                elif chc ==1:
                    count = int(input("How many numbers you want to add:"))
                    sum = 0
                    for i in range(count):
                        sum +=int(input(f"Enter the {i+1} number:"))
                    print(f"Sum:{sum}")
                    tim = t.strftime("%Y-%m-%d %H:%M:%S")
                    database[tim]=["Sum",sum]
                elif chc ==2:
                    count = int(input("How many numbers you want to subtract:"))
                    diff = 0
                    for i in range(count):
                        if diff == 0:
                            diff +=int(input(f"Enter the {i+1} number:"))
                        else:
                            diff -=int(input("Enter the number:"))
                            
                    print(f"Difference:{diff}")
                    tim = t.strftime("%Y-%m-%d %H:%M:%S")
                    database[tim]=["Difference",diff]
                elif chc ==3:
                    count = int(input("How many numbers you want to Multiply:"))
                    sum = 1
                    for i in range(count):
                        sum *=int(input(f"Enter the {i+1} number:"))
                    print(f"Product:{sum}")
                    tim = t.strftime("%Y-%m-%d %H:%M:%S")
                    database[tim]=["Product",sum]
                elif chc ==4:
                    num1 = float(input("Enter the first number:"))
                    num2 = float(input("Enter the second number:"))
                    while num2 ==0:
                        print("Diviser cant be zero:")
                        num2 = float(input("Enter the second number:"))
                    print(f"Result:{num1/num2}")
                    tim = t.strftime("%Y-%m-%d %H:%M:%S")
                    database[tim]=["Reasult",(num1/num2)]
                
                elif chc ==5:
                    num1 = float(input("Enter the first number:"))
                    num2 = float(input("Enter the second number:"))
                    while num2 ==0:
                        print("Divisor cant be zero:")
                        num2 = float(input("Enter the second number:"))
                    print(f"Reminder:{num1%num2}")
                    tim = t.strftime("%Y-%m-%d %H:%M:%S")
                    database[tim]=["Reminder",(num1%num2)]
                else:
                    print("Invalid input:")
                
                
        except ValueError as v:
            print(v)
    
    def sci(self,value):
       
        chc = 0
        while chc !=-1:
            print("1.sin  value                  2.cos value")
            print("3.tan value                   4.squre root")
            print("-1.Exit")
            try:
                chc= 0
                while chc !=-1:
                    chc= int(input("Enter the choice:"))
                    if chc ==-1:
                        break
                    elif chc ==1:
                        print(f"Sin of the {value} is:{m.sin(value)}")
                        tim = t.strftime("%Y-%m-%d %H:%M:%S")
                        database[tim]=["Sin",(m.sin(value))]
                    elif chc ==2:
                       print(f"Cos of the {value} is:{m.cos(value)}")
                       tim = t.strftime("%Y-%m-%d %H:%M:%S")
                       database[tim]=["Cos",(m.cos(value))]
                    elif chc ==3:
                        print(f"tan of the {value} is:{m.tan(value)} ")
                        tim = t.strftime("%Y-%m-%d %H:%M:%S")
                        database[tim]=["tan",(m.tan(value))]
                    elif chc ==4:
                        print(f"Square root of the {value} is:{m.sqrt(value)}")
                        tim = t.strftime("%Y-%m-%d %H:%M:%S")
                        database[tim]=["Square root:",(m.sqrt(value))]
                    else:
                        print("Invalid choice:")
            except ValueError as v:
                print(v)
        
    def randomno(self):
        print("Creating a radom numbers:")
        start = int(input("Enter the Sarting:"))
        end = int(input("Enter the Ending :"))
        
        count = int(input("how many random numbers you want:"))
        
        for i in range(count):
            print(f"{i+1} random:{r.randint(start,end)}")
            tim = t.strftime("%Y-%m-%d %H:%M:%S")
            database[tim]=["Random number",(r.randint(start,end))]
            
    def history(self):
        print("History:")
        print("="*30)
        
        for i in database.keys():
            print(f"Time:{i}  |Operation:{database[i][0]}            |Reasult:{database[i][1]}")
            print("-"*50)
        print("="*30)
    
        
def main():
    c = Cal()
    chc = 0
    while chc !=-1:
            print("1.Basic Math                  2.Scientific calculation")
            print("3.Random Numbers              4.View History")
            print("-1.Exit")
            try:
                chc= 0
                while chc !=-1:
                    chc= int(input("Enter the choice:"))
                    if chc ==-1:
                        break
                    elif chc ==1:
                       c.basic()
                    elif chc ==2:
                      c.sci(float(input("Enter the Number for its Evaluation")))
                    elif chc ==3:
                       c.randomno()
                    elif chc ==4:
                       c.history()
                    else:
                        print("Invalid choice:")
            except ValueError as v:
                print(v)
        

if __name__ == "__main__":
    main()
    
