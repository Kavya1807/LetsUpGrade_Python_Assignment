#Title: Student Grading Program

#Title: Student Grading Program

while True:

    try:

        roll = int(input("Enter the student Roll number: "))
        print(f"Roll number: {roll}")

        name = input("Enter the name of the student: ")
        print("Student name: " + name)

        marks =int(input("Enter marks of a student : "))
        print(f"The Marks of the student :{marks}")

        if marks>=90 and marks<=100:
              print("Your Grade is A+")
        elif marks>=80 and marks<=89:
               print("Your Grade is A")
        elif marks>=70 and marks<=79:
                      print("Your Grade is B")
        elif marks>=60 and marks<=69:
                      print("Your Grade is C")
        elif marks>=50 and marks<=59:
                      print("Your Grade is D")
        else :
                    print("You have Failed!")

    except:

        print("Invalid Input!")


















