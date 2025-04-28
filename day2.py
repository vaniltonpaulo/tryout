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
