#This program prints the multiplication table of a number entered by the user using while loop

num = int(input("Please enter a number"))
i = 1;
while i <= 10:
    print(num, "X",i,"=",num*i)
    i = i + 1

