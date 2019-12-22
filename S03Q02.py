#This program is used to perform different operations using functions

import math

def remainder(num):
    remainder = num % 10
    print(remainder, "is the remainder")

             
def do_1digit_oper(num):
    if num <= 9:
      print("The number you have entered is a single digit number , so the number after adding 7 to it will be")
      newdigit = (num) + 7
      print(newdigit)
      output = remainder(newdigit)
      
    
def do_2digit_oper(num):
    if num >=10 and num < 100:
        print("The number you have entererd is a two digit number ,the number after raising its power by 5 will be")
        newnum = pow(num,5)
        print(newnum)
        output = remainder(newnum)

        
def do_3digit_oper(num):
    if num >99 and num <1000:
       print("The number you have entererd is a 3 digit number",num)
       digit3num = num
       num2 = int(input("Please enter another number"))
       newnum = (digit3num) + (num2)
       print(newnum)
       output = remainder(newnum)

   
num = int(input("Please enter a number "))    
num1 = do_1digit_oper(num)
num2 = do_2digit_oper(num)
num3 = do_3digit_oper(num)









    
