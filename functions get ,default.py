#1.get method using various key methods:
def get_function():

    dict_1={"vegetabiles11":"onion","vegetabiles2":"chilles"}

    print(dict_1.get("vegetabiles11"))

get_function()

#2
def get_function2():

    dict_2= {
        "name":"jhon",
        "location":"germany"
        }
    print(dict_2.get("name"))
get_function2()

#3
def get_function3():

    dict_3 = {
        "animal":"cat",
        "drink":"milk"
        }
    print(dict_3.get("animal1"))
get_function3()
#4
def get_function4():

    dict_4 = {
        "animal":"tiger",
        "fruit":"apple"
        }
    print(dict_4.get("animal"))
get_function4()


# using the setdefault method to get values

#1
def set_default1():
    dict_1 = {"fruit1" :"mango", "fruit2" :"apple"}
    print(dict_1.setdefault('fruit1'))
    print(dict_1)
set_default1()

#2
def set_default2():
    dict_2 = {
        "name":"john",
        "occupation":"seller"
        }
    print(dict_2.setdefault('name'))
set_default2()

#3
def set_default3():
    dict_3 = {
        "name":"john",
        "occupation":"seller"
        }
    print(dict_3.setdefault('name1'))
set_default3()
                            

                     
    
