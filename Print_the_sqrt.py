import math

while True:
    number = int(input("please enter a number: "))

    if number == 0:
        break

    elif number <= 9:
        print("The number you have entered is a single digit number")

    elif number > 99 and number < 1000:
        result = math.sqrt(number)
        print("The square root of",number,"is: ", result)
        
    else:
        print(number, "The Number you have entered is a 2 digit number")

   
        

    

    

    


    
             

