"""Q1. Github Account Setup
1. Create a GitHub account (if you don’t have one).
2. Create a new repository named Python-Basic-Projects.
3. After implementing each feature in each question’s solution, commit your
code with a proper commit message (e.g., "Implement Loop for Counting
Vowels" or “Create analyze_string function”).
4. After completing the full project, push everything to GitHub."""

def count(string):
    ls = list(string)
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    
    for i in vowels:
        print(f"no of:{i} in {string} is:{ls.count(i)}")
        
count(input("Enter the string:"))