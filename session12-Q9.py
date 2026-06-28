"""Q9. (Strings + Sets + Exception Handling + Modules) 
Write a program that: 
Takes a sentence as input. 
Extracts all unique words (using set) from the sentence. 
Prints the unique words in sorted order. 
Uses math module to print the total number of unique words raised to power 2. Handle any 
possible exceptions gracefully. 
"""

print("Q9. (Strings + Sets + Exception Handling + Modules)")
import math as m

sentence = input("Enter the sentence:")
words = sentence.split()
stc = set()
        
    
for i in words:
    stc.add(i)
    

print(f"Our set is:{stc}")

stc = list(stc)

stc.sort()

try:
    print(f"Unique words in sorted order are:{stc}")

    no_uniquewoed = len(stc)


    print(f"Total no of unique words raised to power 2 is:{m.pow(no_uniquewoed,2)}")
    
except Exception as e:
    print(e)