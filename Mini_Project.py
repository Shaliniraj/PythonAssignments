Login_Id = 10
count = 0

while True:
    User_Id = int(input("Please enter number  between 1 to 25 to login into the censex toolbox "))

    count += 1


    if User_Id == Login_Id:
        print("Welcome!!!")
        break

    elif count == 5:
        print("Login Failed")
        break

    elif User_Id >= Login_Id-2 and User_Id <= Login_Id+2:
        print("InVaLiD PaSsCode")

    elif User_Id > Login_Id-2:
        print("INVALID PASSCODE")

    elif User_Id < Login_Id+2:
        print("invlaid passcode")


    
    

    
        
        
