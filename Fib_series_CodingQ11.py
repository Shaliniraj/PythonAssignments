#Program to display the first 12 even Fibonacci numbers

nterms = 50

# first two terms
n1 = 1
n2 = 1
count = 0
evennumber = 0

if nterms <= 0:
   print("Please enter a positive integer")
   
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   
else:
   print("Fibonacci sequence:")

   while count < nterms:

      if n1 % 2 == 0:
         if evennumber != 12:
            print(n1)
            evennumber = evennumber+1
      nth = n1 + n2
      
      n1 = n2
      n2 = nth
      count += 1
           
       
