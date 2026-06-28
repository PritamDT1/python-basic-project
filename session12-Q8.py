"""Q8. (Tuples + Dictionaries + OOP)
Create a class Employee with:
Attributes: emp_id, name, details (a tuple containing department and salary).
Method show_details() to print all information.
Create a dictionary where employee ID is the key and Employee object is the
value.
Add 3 employees and display all using a loop."""

print("Q8. (Tuples + Dictionaries + OOP)")

class Employee:
    def __init__(self,emp_id,name,details):
        self.id=emp_id
        self.name = name
        self.details = details
        
    def show_details(self):
        print(f"Name:{self.name}")
        print(f"Employee Id:{self.id}")
        print(f"Depertment:{self.details[0]}")
        print(f"Depertment:{self.details[1]}")
    
    
    def add(self):
        return self.id
    

def main():
    data = dict()
    try:
        detail = (input("Enter the depertment:"),float(input("Enter the salary:")))
        e1 = Employee(int(input("Enter the Employee id:")),input("Enter the name:"),detail)
        
        detail = (input("Enter the depertment:"),float(input("Enter the salary:")))
        e2 = Employee(int(input("Enter the Employee id:")),input("Enter the name:"),detail)
        
        detail = (input("Enter the depertment:"),float(input("Enter the salary:")))
        e3 = Employee(int(input("Enter the Employee id:")),input("Enter the name:"),detail)
        
    except ValueError as v:
        print(v)
    
    else:
        data[e1.add()] = e1
        data[e2.add()] = e2
        data[e3.add()] = e3
        
        print("Details of all three employees are as follows:")
        print("*"*30)
        
        for i in data.values():
            i.show_details()
            print("-"*30)
        

main()
        
        
        