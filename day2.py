def circle_or_square(rad, area):
    cir = 2 * 3.14* rad
    peri = (area ** 0.5) * 4
    if cir > peri:
        return True
    else:
        return False



print(circle_or_square(16, 625)) # True

circle_or_square(5, 100) # False

circle_or_square(8, 144) # True

def asc_des_none(lst, s):
    if s=="Asc":
        return sorted(lst,reverse=False)
    elif s == "Des":
         return sorted(lst,reverse=True)
    else:
        return lst


print(asc_des_none([4, 3, 2, 1], "Asc" )) # [1, 2, 3, 4]

print(asc_des_none([7, 8, 11, 66], "Des")) # [66, 11, 8, 7]

print(asc_des_none([1, 2, 3, 4], "None")) # [1, 2, 3, 4]

import math

def radians_to_degrees(rad):
    result = rad * (180/math.pi)
    return round(result,1)


print(radians_to_degrees(1)) ## 57.3

radians_to_degrees(20) ## 1145.9

radians_to_degrees(50) ## 2864.8


def parity_analysis(num):
    result = sum(map(int, str(num)))
    return (result % 2) == (num % 2)
    




print(parity_analysis(243)) # True
# 243 is odd and so is 9 (2 + 4 + 3)

parity_analysis(12) # False
# 12 is even but 3 is odd (1 + 2)

parity_analysis(3) # True
# 3 is odd and 3 is odd and 3 is odd (3)

def calculator(num1, operator, num2):
    if num2 == 0:
        return "Can't divide by 0!"
    values = [str(num1),operator,str(num2)]
    operation = " ".join(values)
    return eval(str(operation))



print(calculator(2, "+", 2)) # 4

calculator(2, "*", 2) # 4

calculator(4, "/", 2) # 2

def mood_today(mood = "neutral"):
    return f"Today, I am feeling {mood}"



print(mood_today("happy")) # "Today, I am feeling happy"

mood_today("sad") # "Today, I am feeling sad"

print(mood_today()) # "Today, I am feeling neutral"


import math
def solve_for_exp(a, b):
    return round(math.log(b,a),0)


solve_for_exp(4, 1024) # 5

print(solve_for_exp(2, 1024)) # 10

print(solve_for_exp(9, 3486784401)) # 10

def inclusive_list(start_num, end_num):
    if start_num > end_num:
        return start_num
    else:
        return sorted(list(range(start_num,end_num + 1,1)))
    



print(inclusive_list(1, 5)) # [1, 2, 3, 4, 5]

print(inclusive_list(2, 8)) # [2, 3, 4, 5, 6, 7, 8]

print(inclusive_list(10, 20)) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(inclusive_list(17, 5)) # [17]

import re

txt1 = "red flag blue flag"
txt2 = "yellow flag red flag blue flag green flag"
txt3 = "pink flag red flag black flag blue flag green flag red flag"
pattern =  "red flag|blue flag"

print(re.findall(pattern, txt1)) # ["red flag", "blue flag"]
re.findall(pattern, txt2) # ["red flag", "blue flag"]
re.findall(pattern, txt3) # ["red flag", "blue flag", "red flag"]

def list_less_than_100(lst):
    if sum(lst) < 100:
        return True
    else:
        return False


print(list_less_than_100([5, 57])) # True

list_less_than_100([77, 30]) # False

list_less_than_100([0]) # True

def is_triplet(n1, n2, n3):
    max_lst = sorted([n1, n2, n3])
    smallest_list = [x**2 for x in max_lst[0:2]]
    if sum(smallest_list) == (max_lst[2]**2):
        return True
    else:
        return False
    


print(is_triplet(3, 4, 5)) # True
# 3² + 4² = 25
# 5² = 25

print(is_triplet(13, 5, 12)) # True
# 5² + 12² = 169
# 13² = 169

print(is_triplet(1, 2, 3)) # False
# 1² + 2² = 5
# 3² = 9


def jazzify(lst):
    if len(lst) == 0:
        return lst
    result = []
    for word in lst:
        if word.endswith("7"):
            result.append(word)
        else:
            word = "{}7".format(word)
            result.append(word)
    return result



print(jazzify(["G", "F", "C"])) # ["G7", "F7", "C7"]

print(jazzify(["Dm", "G", "E", "A"])) # ["Dm7", "G7", "E7", "A7"]

print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])) # ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

print(jazzify([])) # []

