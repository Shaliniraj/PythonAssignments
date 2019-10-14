#This progranm prints the multiplication table of a number entered by the user using a for loop

num = int(input("Please enter a number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
