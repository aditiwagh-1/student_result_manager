# empty dictionary declaration
student ={}
try:
    with open ("students.txt", "r") as file:
        for line in file:
            line = line.strip()
            if ":" in line:
                stu_name , stu_marks = line.split(":")
                student[stu_name] = int(stu_marks)
except FileNotFoundError:
    print("file not founded !!!")
    pass
# while loop
while True:
    # initialization of the project
    print("----welcome to the student result management system----")
    print("-------------------------------------------------------")
    print("choose the option ......")
    print("1. add student")
    print("2. view all students")
    print("3. check the result")
    print("4. Result Calculation")
    print("5. exit")
    choice = int(input("enter your choices = "))
    # if else conditions for adding the student in the empty dictionary
    if choice == 1:
        user_choice = input("you want to add student (yes/no) = ")
        if (user_choice == "yes"):
            stu_name = input("enter the student name = ")
            if stu_name in student:
                print("student already exits duffer!!")
            else:
                stu_marks = int(input("enter the student marks = "))
            # adding the elments in he ditionary in thekey value pair
                student[stu_name] = stu_marks
                with open("students.txt", "a") as file:
                    file.write(f"{stu_name} : {stu_marks}\n")
                print(f"{stu_name} Successfully added !\n\n\n\n")
        elif(user_choice == "no"):
            print("exit !")
            print("choose the option ......")
            print("1. add student")
            print("2. view all students")
            print("3. check the result")
            print("4. exit")
        else:
            print("Invalide entry!!!!!!!!\n\n\n")
    # this elif condition is for viewing the all students in the dictionary
    elif choice == 2:
        if not student:
            print("no student found!!!")
        else:
            for stu_name, stu_marks in student.items():
                    print(stu_name,":",stu_marks)
     
    # this elif condition is for checking the result
    elif choice == 3:
        stu_name = input("enter the student name = ")
        if stu_name in student:
            stu_marks = student[stu_name]
            print(stu_marks)
            if stu_marks >= 35:
                print("student passed !!")
            else:
                print("student failed !!")
        else:
            print("not found in the memory !!")
    elif choice == 4: 
        name = input("Enter the student name = ")
        if name in student:
            sub1 = int(input("enter the marks of subject 1 = "))
            sub2 = int(input("enter the marks of subject 2 = "))
            sub3 = int(input("enter the marks of subject 3 = "))
            sub4 = int(input("enter the marks of subject 4 = "))
            sub5 = int(input("enter the marks of subject 5 = "))
            sub6 = int(input("enter the marks of subject 6 = "))
            total = (sub1+sub2+sub3+sub4+sub5+sub6)
            avg = total / 6
            print("Total marks = ",total)
            print("Total percentage = ",avg)
            if(avg >=91 and avg<=100 ):
                print("Grade A1\n")
                print("Outstanding\n")
            elif(avg >= 81 and avg <=90):
                print("Grade A2\n")
                print("Excellent\n")
            elif(avg >=71 and avg <= 80):
                print("Grade B1\n")
                print("Very Good\n")
            elif(avg >=61 and avg<= 70):
                print("Grade B2\n")
                print("Good\n")
            elif(avg >=51 and avg<=60):
                print("Grade C1\n")
                print("Fair\n")
            elif(avg >=33 and avg<= 50):
                print("passed!\n")
            elif(avg <=33):
                print("Failed!\n")
            else:
                print("Invalide entry!\n")
        else :
            print("student not found !!")
# condition for the exiting from the program....
    elif choice == 5:
        print("Exiting .............\n")
        break
    