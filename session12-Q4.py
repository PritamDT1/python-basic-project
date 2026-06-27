"""Q4. (OOP + Lists + Exception Handling)
Create a class Student with attributes: name, roll_no, and marks_list (a list of
marks).
Include methods:
__init__ to initialize the student.
add_mark(mark) to add a mark to the list (handle invalid marks).
get_average() to return the average.
display_info() to show all details.
Create one student object, add marks using user input, and demonstrate all
methods with exception handling."""

class Student:
    marks_list = list()
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        
    def add_mark(self,mark):
        
        try:
            if mark >100:
                raise ValueError("marks must be smaller than 100.")
            if mark <0:
                raise ValueError("Marks Cant be Negative.")
            self.marks_list.append(mark)
        except ValueError  as v:
            print("Marks must be integer of float:")
            print(v)
            self.add_mark(float(input("Re-Enter the marks:")))
    def get_average(self):
        no = len(self.marks_list)
        sum = 0
        for i in self.marks_list:
            sum +=i
        return (sum/no)
    
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Roll no:{self.roll_no}")
        count = 1
        for i in self.marks_list:
            print(f"Marks in subject:{count} is:{i}")
    
    
def main():
    st = Student(input("Enter your name:"),int(input("Enter your roll no:")))
    print("Enter your marks in 5 subjects:")
    for i in range(5):
        st.add_mark(float(input("Enter the marks:")))
    print(f"Average:{st.get_average()}")
    print("*"*30)
    print("Details of the students is as below:")
    st.display_info()
    print("*"*30)
    
if __name__ == "__main__":
    main()
    
        
      