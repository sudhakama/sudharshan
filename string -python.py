statement = input("enter something: ")

if statement:

    lower_= statement.lower()

    for each_character in lower_:

        statement_ = lower_.find(each_character,lower_.index(each_character)+1,len(lower_))

        if statement_!=-1:

            print(f'second occurance of the "{each_character}" is {statement_}.')
        else:
    
             print(f'"{each_character}" has no second occurance and its index is {lower_.index(each_character)}')
else:
    
    print("please enter something")

    
    
    
