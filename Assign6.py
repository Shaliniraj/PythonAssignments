def do_1digit_oper(num):
    if num <= 9:
        return num
    
def do_2digit_oper(num):
    if num >=10 and num <= 99:
        return num

def do_3digit_oper(num):
    if num >99 and num <1000:
        return num

a = int(input("Please enter a number"))
b = int(do_1digit_oper(a))
print("The number you have entered is a single digit number so the number after adding 7 to it will be " ,b+7)

c = int(input("Please enter another number"))
d = int(do_2digit_oper(c))     
print("The number you have entered is a two digit number so the number after raising its power by 5 will be" ,d*5)

e = int(input("Pleae enter a number"))
f = int(do_3digit_oper(e))
print("The number you have enter is a 3 digit number")
g = int(input("Please enter a number "))
print("The new number will be", f+g)
