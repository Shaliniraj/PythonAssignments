#Program to print the multiplication table of a given number

number =(input("please enter a number"))

number = int(number)
for i in range(1, 11):
    print(number,'x',i,'=',number*i)
               
