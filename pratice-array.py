def get_first_value(number_list):
    return number_list[0]


print(get_first_value([1, 2, 3]) )#➞ 1

get_first_value([80, 5, 100]) #➞ 80

get_first_value([-500, 0, 50]) #➞ -500


def addition(a, b):
    return a + b


print(addition(3, 2)) #➞ 5

addition(-3, -6)#➞ -9

addition(7, 3) #➞ 10


def next_edge(side1, side2):
    result =  side1 + side2
    return result - 1

print(next_edge(8, 10)) #➞ 17

next_edge(5, 7) #➞ 11

next_edge(9, 2) #➞ 10


def cubes(a):
	print(a ** 3)
     
cubes(3) #➞ 27

cubes(5) #➞ 125

cubes(10) #➞ 1000


def convert(minutes):
     print(minutes * 60)
     

convert(5) #➞ 300

convert(3) #➞ 180

convert(2) #➞ 120

def string_int(txt):
     print(int(txt))

string_int("6") #➞ 6

string_int("1000") #➞ 1000

string_int("12") #➞ 12

