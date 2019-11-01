# Python program to print the first 12 "even" Fibonacci numbers.
    
numbers = int(input("How many numbers? "))

n1 = 1
n2 = 1
count = 0

if numbers <= 0:
   print("Please enter a positive integer")
elif numbers == 1:
   print("Fibonacci numbers upto",numbers,":")
   print(n1)
else:
   print("Fibonacci numbers upto",numbers,":")
   while count < numbers:
       print(n1,end=' , ')
       n3 = n1 + n2

       n1 = n2
       n2 = n3

       count += 1

