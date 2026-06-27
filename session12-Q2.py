"""Q2. (Strings + Loops + Functions)
Write a function analyze_string(s) that takes a string as input and:
Prints its length using len().
Prints the string in reverse using slicing.
Counts and prints how many vowels (a,e,i,o,u) are in the string (case
insensitive).
Uses a for loop with range() to print each character with its positive and
negative index.
Call this function with user input and handle empty string case."""

def analyze_string(s):
    
    if s =="":
        raise ValueError("Empty strings are not allowed!")
    print(f"Length of the string is:{len(s)}")
    print(f"Reverse string is:{s[::-1]}")
    
    ls = list(s)
    
    
    print(f"No of A in string is:{int(ls.count("a"))+int(ls.count("A"))}")
    print(f"No of E in string is:{int(ls.count("e"))+int(ls.count("E"))}")
    print(f"No of I in string is:{int(ls.count("i"))+int(ls.count("I"))}")
    print(f"No of O in string is:{int(ls.count("o"))+int(ls.count("O"))}")
    print(f"No of U in string is:{int(ls.count("u"))+int(ls.count("U"))}")
        
    pidx = 0
    nidx = -1
    for i in s:
        print(f"positive index of the {i} is:{pidx} and negative index is:{nidx} ")
        pidx +=1
        nidx -=1
        
try:
    analyze_string(input("Enter the String:"))
    
except ValueError as v:
    print(v)
    print("Empty strings are not allowed as an input:")
    
    