""" This program shows the percentages of students scored in thier exams
"""

def grades(percentage,scoreinenglish,scoreinmathematics,totalscoreinscience):
    if percentage >= 90:
        print("First class")
    elif percentage >= 75:
        print("Second class")
    elif scoreinenglish < 25:
        print("Fail")
    elif scoreinmathematics < 35:
        print("Fail")
    elif totalscoreinscience < 35:
        print("Fail")
    elif percentage <= 35:
        print("fail")
    else:
        print("Average")

        return percentage
while True:
    
    ScoreinEnglish = int(input("Please enter the marks scored in english "))

    ScoreinMathematics = int(input("Please enter the marks scored in Mathematics "))
        
    ScoreinScienceTheory = int(input("Please enter the marks scored in science Theoery  "))

    ScoreinSciencePractical = int(input("Please enter the marks scored in science Practical  "))

    TotalScoreScience = int(ScoreinScienceTheory + ScoreinSciencePractical)

    
    Totalmarks =  int(ScoreinEnglish +  TotalScoreScience + ScoreinMathematics)
    percentage = int((Totalmarks / 275) * 95)
    Marks = grades(percentage,ScoreinEnglish,ScoreinMathematics,TotalScoreScience)

    
    
                     


    




