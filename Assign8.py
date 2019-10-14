""" This program shows the percentages of students scored in thier exams
"""

def grades(percentage):
    if percentage >= 90:
        print("First class")
    elif percentage >= 75:
        print("Second class")
    elif percentage <= 35:
        print("Fail")
    else:
        print("Average")

        return percentage

ScoreinEnglish = int(input("Please enter the marks scored in english "))
ScoreinScience = int(input("Please enter the marks scored in science "))
ScoreinMathematics = int(input("Please enter the marks scored in Mathematics "))
Totalmarks =  int(ScoreinEnglish +  ScoreinScience + ScoreinMathematics)
average = Totalmarks / 2.7
percentage = int((Totalmarks / 270) * 90)
print(percentage)
Marks = grades(percentage)
                     


    




