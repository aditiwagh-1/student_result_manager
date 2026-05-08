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
            print(f"{stu_name} Successfully added !\n\n\n\n\n")
        elif(user_choice == "no"):
            print("exit !\n\n\n\n\n")
            print("choose the option ......")
            print("1. add student")
            print("2. view all students")
            print("3. check the result")
            print("4. exit")
        else:
            print("Invalide entry!!!!!!!!\n\n\n")
    # elif choice == 2:
    #     if not student:
    #         print("no student found !!!")
    #     else:
    #         for stu_name , stu_marks in student:
    #             print(stu_name, ":",stu_marks)
    # elif choice == 3:
    #     roll_num = int(input("Enter the roll number of student = "))
    #     if stu_name in student: 
    #         stu_marks = student[stu_name]
            
    # elif choice == 4:
    #     print("exited ........")

# print("program ended success0fully")    