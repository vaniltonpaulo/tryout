# print("i man")
# x = 21
# x += 1

# print('I have ',str(x))

# y = "hello Bro"

# print(y.find("o"))

# print(y.replace("o","e"))

# name = str(input("what is your name?:"))
# age = int(input("what is your age:"))
# height = float(input("what is your height:"))

# print("here are your details:" + "name:"+ name + "age:" + str(age) + "years old"+ "and" + "height"+str(height)+"cm")


# import math
# num = 3.4
# print(math.floor(num))



# x = "Bro code"
# print(x[0:4:1])
# print(x[::-1])
# print(x[slice(3,6)])

### if statement

# age = int(input("how old are you?:"))
# if age == 10:
#     print("almost there buddy, 8 more years")
# elif age >= 16:
#     print("you are of legal age")
# elif not(age > 250):
#     print("too young")
# else:
#     print("not old enough")


## for loops

# for i in range(4,10+1,3):
#     print(i)

# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("happy new year")

# rws = 10
# cols = 5
# symbol = "#"
# for i in range(rws):
#     for j in range(cols):
#      print(symbol, end="")
#     print()

# phone_number = "128-9383-9302"
# for i in phone_number:
#    if i =="-":
#       continue
#    print(i,end="")

# for i in range(1,30):
#    if i == 24:
#       pass
#    else:
#     print(i)



#list
#


# x = {"fork","spoon", "knife"}
# y = {"chicken","fish","potato","fork"}

# print(x.union(y))

# def addition(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#      sum += i
#     return sum
    
# print(addition(1,2,3,4))


# #kwargs

# def hello(**kwargs):
#    print("hello", end=" ")
#    for key,value in kwargs.items():
#       print(value,end=" ")

# hello(titke ="Mr", first = "Bro", middle ="ksoka", last = "code")


#format

# animal = "cow"
# iten ="moon"

# print("the {} jumped over the {}.".format(animal,iten))
# #or
# print("the {1} jumped over the {0}.".format(animal,iten))
# #or 
# print("the {animal} jumped over the {iten}.".format(animal = "lion",iten = "sun"))


#Exception

# try:
#     numerator = int(input("Enter a number to divide:"))
#     denumerator = int(input("Enter a number to divide by:"))
#     result = numerator / denumerator
# except ZeroDivisionError as e:
#     print(e)
#     print("Dont use 0 to divide by 0")
# except ValueError as e:
#     print(e)
#     print("Dont use strings to divide by")
# except Exception as e:
#     print(e)
#     print("something went wrong")
# else:
#     print(result)
# finally:
#     print("this will always execute")


#module

import messages as msg

msg.hello()
msg.bye()

from car import Car

car_1  = Car("toyota","lexus","2018","white")

print(car_1.model)

car_1.drive()