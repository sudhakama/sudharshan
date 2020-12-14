# creating a list using a dictionary

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
#creating empty dictionary
res = {}
for i in test_list:
    res[i]=res.get(i,0)+1
    
print(res)
