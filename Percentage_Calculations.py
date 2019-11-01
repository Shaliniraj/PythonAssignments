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
while True:
    
    ScoreinEnglish = int(input("Please enter the marks scored in english "))
    ScoreinScienceTheory = int(input("Please enter the marks scored in science Theoery  "))
    ScoreinSciencePractical = int(input("Please enter the marks scored in science Practical  "))
    TotalScoreScience = int(ScoreinScienceTheory + ScoreinSciencePractical)
    print(TotalScoreScience)
    ScoreinMathematics = int(input("Please enter the marks scored in Mathematics "))

    if TotalScoreScience <= 33:
        print("fail")
    else:
        Totalmarks =  int(ScoreinEnglish +  TotalScoreScience + ScoreinMathematics)
        average = Totalmarks / 2.75
        percentage = int((Totalmarks / 275) * 95)
        print(percentage)
        Marks = grades(percentage)

    
    
                     


    




