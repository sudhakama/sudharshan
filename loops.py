
i=1
while True:
    user_name=input("enter the name:")
    password=input("password:")
    if i<3:
        if user_name == "sudharshan" and password == "keyword":
            print("logged in")
    
            break
    else:
        print("maximum attempted ")
        break
        
    i+=1
    
    
