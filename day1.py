##  This challenges are classified as very easy

def tri_area(base, height):
        print((base* height) / 2)




tri_area(3, 2) ## 3

tri_area(7, 4) ## 14

tri_area(10, 10) ## 50


def addition(num):
        print(num + 1)

addition(0) ## 1

addition(9) ## 10

addition(-3) ## -2



def bool_to_string(flag):
			return str(flag)


bool_to_string(True) ## "True"

bool_to_string(False) ## "False"


def remainder(x, y):
        print(x % y)

remainder(1, 3) ## 1

remainder(3, 4) ## 3

remainder(5, 5) ## 0

remainder(7, 2) ## 1

def find_perimeter(length, width):
        perimeter	=	2 *(length	+width)
        return perimeter


find_perimeter(6, 7) ## 26

find_perimeter(20, 10) ## 60

find_perimeter(2, 9) ## 22


def calculate_exponent(num, exp):
        return num ** exp


print(calculate_exponent(5, 5)) ## 3125

calculate_exponent(10, 10) ## 10000000000

calculate_exponent(3, 3) ## 27


def sum_polygon(n):
      return  (n - 2) * 180

sum_polygon(3) ## 180

sum_polygon(4) ## 360

sum_polygon(6) ## 720


def circuit_power(voltage, current):
        return voltage * current


circuit_power(230, 10) ## 2300

circuit_power(110, 3) ## 330

circuit_power(480, 20) # # 9600


def animals(chickens, cows, pigs): 
        chi_legs = chickens * 2
        cows_legs = cows * 4
        pi_legs = pigs * 4
        
        return sum([chi_legs,cows_legs,pi_legs])

print(animals(2, 3, 5)) ## 36

animals(1, 2, 3) ## 22

animals(5, 2, 8) ## 50

def how_many_seconds(hours):
        return hours * 60 * 60


print(how_many_seconds(2)) ## 7200

how_many_seconds(10) ## 36000

how_many_seconds(24) ## 86400

def to_int(txt):
        return int(txt)
	

def to_str(num):
        return str(num)

print(to_int("77")) ## 77

to_int("532") ## 532

print(to_str(77)) ## "77"

to_str(532) ## "532"


def points(twopointers, threepointers):
        return sum([twopointers * 2,threepointers * 3])


points(1, 1) ## 5

points(7, 5) ## 29

print(points(38, 8)) ## 100

def is_same_num(num1, num2):
   if num1 == num2:
           return True
   else:
           return False

print(is_same_num(4, 8)) ## False

is_same_num(2, 2) ##  True

is_same_num(2, "2") ## False


def greeting(name):
    if name == "Mubashir":
        return "Hello, my Love!"
    else:
        return "Hello, " + name + "!"


greeting("Matt") ## "Hello, Matt!"

greeting("Helen") ## "Hello, Helen!"

greeting("Mubashir") ## "Hello, my Love!"

def total_amount_adjectives(dct):
        return len(dct)

total_amount_adjectives({ "a": "moron" }) ## 1

total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }) ## 3

total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", "d": "dirtbag" }) ## 4

def convert(hours, minutes):
        hours_to_sec = hours * 60 * 60
        minuts_to_sec = minutes * 60
        return sum([hours_to_sec,minuts_to_sec]) 



print(convert(1, 3)) ## 3780

convert(2, 0)# # 7200

convert(0, 0) ## 0


def give_me_something(a):
 return "something " + a

print(give_me_something("is better than nothing")) ## "something is better than nothing"

give_me_something("Bob Jane") ## "something Bob Jane"

give_me_something("something") ## "something something"


def findLargestNum(nums):
        return max(nums)

print(findLargestNum([4, 5, 1, 3])) ## 5

findLargestNum([300, 200, 600, 150]) ## 600

findLargestNum([1000, 1001, 857, 1]) ## 1001


def find_smallest_num(lst):
        return min(lst)

print(find_smallest_num([34, 15, 88, 2])) ## 2

find_smallest_num([34, -345, -1, 100]) ## -345

find_smallest_num([-76, 1.345, 1, 0]) ## -76

find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ## -0.9999

find_smallest_num([7, 7, 7]) ## 7

def calc_age(age):
        return age * 365
calc_age(65) ## 23725

calc_age(0) # 0

calc_age(20) # 7300

def football_points(wins, draws, losses):
        sum_wins = wins * 3
        sum_draws = draws * 1
        return sum([sum_wins,sum_draws])

football_points(3, 4, 2) # 13


football_points(0, 0, 1) # 0
football_points(5, 0, 2) # 15



def is_equal(obj_one, obj_two):
        return obj_one == obj_two

# The first object parameter.

obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


print(is_equal(obj_one, obj_two))
## False




# The first object parameter.

obj_one = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


is_equal(obj_one, obj_two)
## True

def difference_max_min(lst):
        return max(lst) -min(lst)

difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) # 82
# Smallest number is -50, biggest is 32.

difference_max_min([44, 32, 86, 19]) # 67
# Smallest number is 19, biggest is 86.


def mod(m, n):
        return m % n

mod(-13, 64) # 51

mod(50, 25) # 0

mod(-6, 3) # 0

def concat(lst1, lst2):
        return lst1 + lst2

print(concat([1, 3, 5], [2, 6, 8])) ## [1, 3, 5, 2, 6, 8]

concat([7, 8], [10, 9, 1, 1, 2]) ## [7, 8, 10, 9, 1, 1, 2]

concat([4, 5, 1], [3, 3, 3, 3, 3]) ## [4, 5, 1, 3, 3, 3, 3, 3]

a = [1, 2, 3]
b = [4, 5, 6]

# Add all elements from list 'b' to the end of list 'a'
a.extend(b)

print(a)


def profitable_gamble(prob, prize, pay):
        if (prob * prize) > pay:
                return True
        else:
                False

profitable_gamble(0.2, 50, 9) # True

profitable_gamble(0.9, 1, 2) # False

profitable_gamble(0.9, 3, 2) # True

def less_than_or_equal_to_zero(num):
        if num <= 0:
                return True
        else:
                return False

less_than_or_equal_to_zero(5) # False

less_than_or_equal_to_zero(0) # True

less_than_or_equal_to_zero(-2) # True



def less_than_100(a, b):
        if sum([a,b]) < 100:
                return True
        else:
                return False

print(less_than_100(77, 30))