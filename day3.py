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
