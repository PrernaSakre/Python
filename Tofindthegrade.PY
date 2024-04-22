#to find the grade
english_mark=int(input("enter the english marks"))
math_mark=int(input("enter the maths mark"))
if english_mark>80 and math_mark>80:
    print("A grade")
elif english_mark>80 or math_mark>80:
    print("B grade")
else:
    print("C grade")


#to find the grad of the students
percentage=float(input("enter the percentage of student:"))
if percentage>=81:
    print("very good")
elif percentage>=61:
    print("good")
elif percentage>=41:
    print("average")
else:
    print("student is fail")
