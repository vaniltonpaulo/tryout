def make_pair(num1, num2):
    result = [num1,num2]
    return result



make_pair(1, 2) # [1, 2]

make_pair(51, 21) # [51, 21]

make_pair(512124, 215) # [512124, 215]



def card_hide(card):
    x = len(card)
    y = card[-4:]
    z = x - len(y)
    return "*" * z + str(y)


print(card_hide("1234123456785678")) # "************5678"

# card_hide("8754456321113213") # "************3213"

# card_hide("35123413355523") # "**********5523"


def XO(txt):
    txt = txt.lower()
    x_sub = "x"
    o_sub = "o"
    if txt.count(x_sub) == txt.count(o_sub):
        return True
    else:
        return False


print(XO("ooxx")) # True

XO("xooxx") # False

XO("ooxXm") # True
# Case insensitive.

XO("zpzpzpp") # True
# Returns True if no x and o.

XO("zzoo") # False

def count_ones(num):
    num = str(bin(num))
    result = num.count("1")
    return result
    


count_ones(0) # 0

count_ones(100) # 3

count_ones(999) # 8


def find_odd(lst):
  for num in lst:
    if lst.count(num) % 2:
      print(num)


 
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ## -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) # 5

find_odd([10]) # 10


def damage(damage, speed, time):
   if damage < 0 or speed <0:
      return "invalid"
   elif time == "second":
      return damage * speed
   elif time == "minute":
      return damage * speed * 60
   else:
      return damage * speed * 60 * 60
   

#    def damage(damage, speed, time):
# 	secs = {'second':1, 'minute':60, 'hour':3600}
# 	ans = damage*speed*secs[time]
# 	return ans if ans>0 and speed>0 else 'invalid'
      

print(damage(40, 5, "second")) # 200

print(damage(100, 1, "minute")) # 6000

damage(2, 100, "hour") # 720000


def sum_recursively(lst):
   return sum(lst)

print(sum_recursively([1, 2, 3, 4])) # 10

sum_recursively([1, 2]) # 3

sum_recursively([1]) # 1

sum_recursively([]) # 0

import re

def count_vowels(txt):
   x = re.findall("a|e|o|i|u", txt)
   return len(x)

print(count_vowels("Celebration")) # 5

count_vowels("Palm") # 1

count_vowels("Prediction") # 4




# import math

# def number_split(n):
#     x = (n / 2)
#     if x > 0:
#         x = round(x,0)
#         if x % 2 != 0:
#             result = [x, x + 1]
#             return result
#         else:
#             result = [x, x]
#             return result
#     else:
#         if x % 2 != 0:
#             x = math.floor(x)
#             x = round(x,0)
#             result = [x, x + 1]
#             return result
#         else:
#             x = math.floor(x)
#             x = round(x,0)
#             result = [x, x]
#             return result

# Not my solution
def number_split(n):
	return [n//2, n - n//2]         

print(number_split(4)) # [2, 2]

print(number_split(10)) # [5, 5]

print(number_split(11)) # [5, 6]

print(number_split(-9)) # [-5, -4]


def reverse(txt):
   txt = txt.swapcase()
   return txt[::-1]

print(reverse("Hello World")) # "DLROw OLLEh"

reverse("ReVeRsE") # "eSrEvEr"

reverse("Radar") # "RADAr"

def even_or_odd(lst):
   if sum(lst) % 2 ==0:
      return "even"
   else:
      return "odd"


even_or_odd([0]) # "even"

even_or_odd([1]) # "odd"

even_or_odd([]) # "even"

even_or_odd([0, 1, 5]) # "even"

def check(lst, el):
   if el in lst:
      return True
   else:
      return False


check([1, 2, 3, 4, 5], 3) # True

check([1, 1, 2, 1, 1], 3) # False

check([5, 5, 5, 6], 5) # True

check([], 5) # False



def check_equals(lst1, lst2):
	if lst1[::] == lst2[::]:
		print(True)
	else:
		print(False)

check_equals([1, 2], [1, 3]) # False

check_equals([1, 2], [1, 2]) # True

check_equals([4, 5, 6], [4, 5, 6]) # True

check_equals([4, 7, 6], [4, 5, 6]) # False

check_equals([1, 12], [11, 2]) # False


def sum_lst(lst):
    total = [0]
    for i in range(0, len(lst)):
       total.append(lst[i])
    return sum(total)

print(sum_lst([1, 2, 3, 4, 5])) # 15

sum_lst([-1, 0, 1]) # 0

sum_lst([0, 4, 8, 12]) # 24


def half_quarter_eighth(n):
    return [n * 0.5,n * 0.25, n* 0.125]

half_quarter_eighth(6) # [3, 1.5, 0.75]

half_quarter_eighth(22) # [11, 5.5, 2.75]

half_quarter_eighth(25) # [12.5, 6.25, 3.125]


def last_ind(lst):
    if not lst:
        return None
    else:
        return lst[-1]


print(last_ind([0, 4, 19, 34, 50, -9, 2])) # 2

print(last_ind("The quick brown fox jumped over the lazy dog")) # "g"

print(last_ind([])) # None

def min_max(nums):
    return [min(nums), max(nums)]


print(min_max([1, 2, 3, 4, 5])) # [1, 5]

min_max([2334454, 5]) # [5, 2334454]

min_max([1]) # [1, 1]

def birthday_cake_candles(candles):
    x = str(max(candles))
    result = str(candles).count(x)
    return int(result)



print(birthday_cake_candles([4, 4, 1, 3])) # 2
# The maximum height candles are four units high.
# There are two of them, so you return 2.

birthday_cake_candles([3, 2, 1, 3]) # 2

birthday_cake_candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25]) # 4

def get_vote_count(votes):
    return votes.get("upvotes") - votes.get("downvotes")


print(get_vote_count({ "upvotes": 13, "downvotes": 0 })) # 13

print(get_vote_count({ "upvotes": 2, "downvotes": 33 })) # -31

get_vote_count({ "upvotes": 132, "downvotes": 132 }) # 0



def get_fillings(sandwich):
    return sandwich[1:len(sandwich)-1]



print(get_fillings(["bread", "ham", "cheese", "ham", "bread"])) # ["ham", "cheese", "ham"]

get_fillings(["bread", "sausage", "tomato", "bread"]) # ["sausage", "tomato"]

get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) # ["lettuce", "bacon", "tomato"]


def all_truthy(*args):
    return all(args)

print(all_truthy(True, True, True)) # True

all_truthy(True, False, True) # False

all_truthy(5, 4, 3, 2, 1, 0) # False






def add_up(num):
      return sum(range(1,num+ 1))
print(add_up(4)) # 10

add_up(13) # 91

add_up(600) # 180300

def triangle(n):
      return n*(n+1)/2


triangle(1) # 1

triangle(6) # 21

print(triangle(215)) # 23220

def missing_num(lst):
    x = range(1, 10+1)
    
    for i in x:
        if i not in lst:
            return i
    
                  


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])) # 5

print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])) # 10

print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9])) # 7

def eda_bit(start, end):
     result = []
     for i in range(start, end + 1):
          if i % 3 == 0 and i % 5 == 0:
               result.append("EdaBit")
          elif i % 3 == 0:
               result.append("Eda")
          elif i % 5 == 0:
               result.append("Bit")
          else:
               result.append(i)
     return result
               


print(eda_bit(0, 10)) # ["EdaBit", 1, 2, "Eda", 4, "Bit", "Eda", 7, 8, "Eda", "Bit" ]

print(eda_bit(14, 20)) # [14,  "EdaBit", 16, 17,  "Eda", 19, "Bit" ]

print(eda_bit(99, 106)) # ["Eda", "Bit", 101, "Eda", 103, 104, "EdaBit", 106 ]

# Create a function that returns the mean of all digits.
# The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).


def mean(num):
     x = [int(x) for x in str(num)]
     result  = sum(x)/ len(x)
     return  int(result)


mean(42) ## 3

print(mean(12345)) ## 3

mean(666) ## 6

def square_digits(n):
    x = [int(digit) for digit in str(n)]     # split digits
    x = [i ** 2 for i in x]                  # square each digit
    x = [str(i) for i in x]                  # convert back to string
    result =  "".join(x)                     # join without spaces
    return int(result)                        



print(square_digits(9119)) # 811181

square_digits(2483) # 416649

square_digits(3212) # 9414

def cars_needed(n):
    if n  == 0:
        return 0
    elif n % 5 == 0:
        return n/ 5
    else:
        return (n // 5) + 1

print(cars_needed(5)) # 1

print(cars_needed(11)) # 3

print(cars_needed(0)) # 0


def unique(lst):
    return min(lst, key= lst.count)

def unique(lst):
	for num in lst:
		if lst.count(num) == 1:
			return num


print(unique([3, 3, 3, 7, 3, 3])) # 7

unique([0, 0, 0.77, 0, 0]) # 0.77

unique([0, 1, 1, 1, 1, 1, 1, 1]) # 0