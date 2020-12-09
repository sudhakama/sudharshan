statement = input('enter the sentence:')

if statement:

    lower_=statement.lower()

    vowels='a','e','i','o','u'

    numbers='0','1','2','3','4','5','6','7','8','9'

for letters in lower_:
    statement_= lower_.find(letters,lower_.index(letters)+1,len(lower_))

    if statement_==-1:

             if letters in vowels:

                 print(f'unique ccharacter is {letters} and this is vowel and ord is (ord{letters})')

              #elif letter == numbers:

                     #pass

             else:

                 print(f'unique character is {letters} and this is consonent and ord is {ord(letters)}')
else:

    print("please enter something.")


    
    


    

    
    
