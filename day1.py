##  This challenges are classified as very easy

def tri_area(base, height):
        print((base* height) / 2)




tri_area(3, 2) #➞ 3

tri_area(7, 4) #➞ 14

tri_area(10, 10) #➞ 50


def addition(num):
        print(num + 1)

addition(0) #➞ 1

addition(9) #➞ 10

addition(-3) #➞ -2



def bool_to_string(flag):
			return str(flag)


bool_to_string(True) #➞ "True"

bool_to_string(False) #➞ "False"


def remainder(x, y):
        print(x % y)

remainder(1, 3) #➞ 1

remainder(3, 4) #➞ 3

remainder(5, 5) #➞ 0

remainder(7, 2) #➞ 1

def find_perimeter(length, width):
        perimeter	=	2 *(length	+width)
        return perimeter


find_perimeter(6, 7) #➞ 26

find_perimeter(20, 10) #➞ 60

find_perimeter(2, 9) #➞ 22


def calculate_exponent(num, exp):
        return num ** exp


print(calculate_exponent(5, 5)) #➞ 3125

calculate_exponent(10, 10) #➞ 10000000000

calculate_exponent(3, 3) #➞ 27


def sum_polygon(n):
      return  (n - 2) * 180

sum_polygon(3) #➞ 180

sum_polygon(4) #➞ 360

sum_polygon(6) #➞ 720


def circuit_power(voltage, current):
        return voltage * current


circuit_power(230, 10) #➞ 2300

circuit_power(110, 3) #➞ 330

circuit_power(480, 20) # ➞ 9600


def animals(chickens, cows, pigs): 
        chi_legs = chickens * 2
        cows_legs = cows * 4
        pi_legs = pigs * 4
        
        return sum([chi_legs,cows_legs,pi_legs])

print(animals(2, 3, 5)) #➞ 36

animals(1, 2, 3) #➞ 22

animals(5, 2, 8) #➞ 50

def how_many_seconds(hours):
        return hours * 60 * 60


print(how_many_seconds(2)) #➞ 7200

how_many_seconds(10) #➞ 36000

how_many_seconds(24) #➞ 86400

def to_int(txt):
        return int(txt)
	

def to_str(num):
        return str(num)

print(to_int("77")) #➞ 77

to_int("532") #➞ 532

print(to_str(77)) #➞ "77"

to_str(532) #➞ "532"


def points(twopointers, threepointers):
        return sum([twopointers * 2,threepointers * 3])


points(1, 1) #➞ 5

points(7, 5) #➞ 29

print(points(38, 8)) #➞ 100