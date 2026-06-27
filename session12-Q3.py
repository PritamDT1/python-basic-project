"""Q3. (Lists + Functions + Exception Handling)
Create a function manage_marks() that:
Takes 5 subject marks as input from the user.
Stores them in a list.
Handles ValueError if non-numeric input is given.
Calculates and prints the average, highest, and lowest marks.
Sorts the list in descending order and prints it.

Session 12 (AIML) - Assignment Questions 1

Use meaningful comments."""

def manage_marks():
    marks = []
    
    try:
        for i in range(5):
            marks.append(int(input(f"Enter the marks in  subject at {i+1} subject:")))
        
        marks.sort()
        print(f"highest marks are:{marks[-1]}")
        print(f"Lowest marks are:{marks[0]}")
        sum = 0
        for i in marks:
            sum +=i
        print(f"Average marks are:{(sum/5)}")
        marks.reverse()
        print(f"Our marklist in desending order is:{marks}")
    except ValueError as v:
        print(v)
        
manage_marks()