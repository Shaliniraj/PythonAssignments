def perform_check(number):

    if number > 99 and number  < 1000:
        print(number,"The Number you have entered is a 3 digit number")

    elif number  > 10 and number  < 100:
        print(number,"The Numbers you have entered is a 2 digit number")

    else:
        print("The number you have entered is :",number) 
    

num1 = int(input("Please enter first numbers "))
num2 = int(input("Please enter second number "))
perform_check(num1)
perform_check(num2)
