# empty dictionary declaration
student ={}
# while loop
while True:
    # initialization of the project
    print("----welcome to the student result management system----")
    print("-------------------------------------------------------")
    print("choose the option ......")
    print("1. add student")
    print("2. view all students")
    print("3. check the result")
    print("4. exit\n\n")
    choice = int(input("enter your choices = "))
    # if else conditions for adding the student in the empty dictionary
    if choice == 1:
        user_choice = input("you want to add student (yes/no) = ")
        if (user_choice == "yes"):
            stu_name = input("enter the student name = ")
            stu_marks = int(input("enter the student marks = "))
            # adding the elments in he ditionary in thekey value pair
            student[stu_name] = stu_marks
            print(f"{stu_name} Successfully added !\n\n\n\n")
        elif(user_choice == "no"):
            print("exit !\n\n\n\n")
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
    # condition for the exiting from the program....
    elif choice == 4:
        print("Exiting .............")
        break
    else:
        print("Invalide Input")
        

# print("program ended success0fully")    