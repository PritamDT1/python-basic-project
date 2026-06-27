"""Q5. (Dictionaries + Functions + Control Structures)
Write a function student_database() that uses a dictionary (roll number as key) to
store student records.
Provide a menu using while loop:
1. Add student (name, age, city)
2. Search student by roll number
3. Display all students
4. Exit
Use get(), update(), and proper exception handling for invalid inputs."""

database = dict()
def student_database():
    chc = int(input("Enter the choice -1 to skip loop:"))
    while chc !=-1:
        print("1. Add student                       2. Search student by roll number")
        print("3. Display all students             -1.Exit")
        try:
            chc = int(input("Enter the choice:"))
        except ValueError as v:
            print(v)
        
        if chc ==1:
            try:
                no = int(input("Enter the roll no:"))
                name = input("Enter the name:")
                age = int(input("Enter the age"))
                while age<0:
                    print("Age cant be negative:")
                    age = int(input("Enter the age"))
                city = input("Enter the City:")
                database[no]=[name,age,city]
            except ValueError as v:
                print(v)
        elif chc ==2:
            try:
                no = int(input("Enter the roll no of student to search:"))
                if no in database:
                    print("*"*30)
                    print("Details of the Student are as given below:")
                    print(f"Roll no:{no}")
                    print(f"Name:{database[no][0]}")
                    print(f"Age :{database[no][1]}")
                    print(f"City:{database[no][2]}")
                    print("-"*30)
            except ValueError as v:
                print(v)
        elif chc ==3:
            for i in database.keys():
                    print("*"*30)
                    print("Details of the Student's are as given below:")
                    print(f"Roll no:{i}")
                    print(f"Name:{database[i][0]}")
                    print(f"Age :{database[i][1]}")
                    print(f"City:{database[i][2]}")
                    print("-"*30)
        else:
            print("INVALID CHOICE!")
    
student_database()