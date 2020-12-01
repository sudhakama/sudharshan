marks=int(input('enter the marks:'))

if 70<= marks <80:
    print("check 70-75 category and 80-85 category")
    if 70 <= marks <=75:
         print('Average')
    else:
        print('above average')
elif 80<= marks<90:
    print('Distination')
elif 90<=marks<=100:
     print('elite')
elif 0>=marks<70:
    print('poor student')
else:
     print('the number of students below 100')
                      
                  
 


