def sort_by_length(lst):
    return sorted(lst, key=len)


print(sort_by_length(["Google", "Apple", "Microsoft"]))
# ["Apple", "Google", "Microsoft"]

print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
# ["Raphael", "Leonardo", "Donatello", "Michelangelo"]

sort_by_length(["Turing", "Einstein", "Jung"])
# ["Jung", "Turing", "Einstein"]




def unique(lst):
    return min(lst, key= lst.count)

def unique(lst):
	for num in lst:
		if lst.count(num) == 1:
			return num


print(unique([3, 3, 3, 7, 3, 3])) # 7

unique([0, 0, 0.77, 0, 0]) # 0.77

unique([0, 1, 1, 1, 1, 1, 1, 1]) # 0

#Sort a List by String Length

def sort_by_length(lst):
    return sorted(lst, key=len)


print(sort_by_length(["Google", "Apple", "Microsoft"]))
# ["Apple", "Google", "Microsoft"]

print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
# ["Raphael", "Leonardo", "Donatello", "Michelangelo"]

sort_by_length(["Turing", "Einstein", "Jung"])
# ["Jung", "Turing", "Einstein"]

# def unique(lst):
# 	for num in lst:
# 		if lst.count(num) == 1:
# 			return num
def equal(a, b, c):
      x  = [a,b,c]
    
      if x.count(a) == 3:
                  return 3
                  print("All 3 values are equal")
      elif x.count(a) == 2 or x.count(b) == 2:
                  return 2
                  print("Two values are equal")
      else:
                  return 0
                  print("All values are differents")
            

print(equal(3, 4, 3)) # 2

print(equal(1, 1, 1)) # 3

print(equal(3, 4, 1)) # 0
print(equal(7, 7, 7)) 
print(equal(6, 3, 3))


def get_discounts(nums, d):
        d = d.strip("%")
        d = int(d) / 100
        r = [i * d for i in nums]
        return r
        
   

get_discounts([2, 4, 6, 11], "50%") # [1, 2, 3, 5.5]

get_discounts([10, 20, 40, 80], "75%") # [7.5, 15, 30, 60]

get_discounts([100], "45%") # [45}




def scale_tip(lst):
        res = lst.index("I")
        p = lst[:res]
        s = lst[res+1:]
        if sum(p) > sum(s):
                return "left"
        elif sum(p) == sum(s):
                return "balanced"
        else:
                return "right"
       




print(scale_tip([0, 0, "I", 1, 1])) # "right"
# 0 < 2 so it will tip right

scale_tip([1, 2, 3, "I", 4, 0, 0]) # "left"
# 6 > 4 so it will tip left

scale_tip([5, 5, 5, 0, "I", 10, 2, 2, 1]) # "balanced"
# # 15 = 15 so it will stay balanced

def num_to_dashes(num):
        return "-" * num



num_to_dashes(1) # "-"

num_to_dashes(5) # "-----"

num_to_dashes(3) # "---"

def word(s):
    d = {
        "one"	:1,
        "two"	:2,
        "three"	:3,
        "four"	:4,
        "five"	:5,
        "six"	:6,
        "seven"	:7,
        "eight"	:8,
        "nine"	:9,
        "zero"	:0
        }
    return d.get(s)


print(word("one")) # 1

word("two") # 2

word("nine") # 9


def char_count(txt1, txt2):
        return txt2.count(txt1)
char_count("a", "edabit") # 1

print(char_count("c", "Chamber of secrets")) # 1

print(char_count("b", "big fat bubble")) # 4



def divisible(num):
        return True if num % 100 ==0 else False

divisible(1) # False

print(divisible(1000)) # True

divisible(100) # True

def profitable_gamble(prob, prize, pay):
        return prob * prize > pay


print(profitable_gamble(0.2, 50, 9)) # True

profitable_gamble(0.9, 1, 2) # False

profitable_gamble(0.9, 3, 2) # True


def comp(txt1, txt2):
        return len(txt1) == len(txt2)

comp("AB", "CD") # True

comp("ABC", "DE") # False

print(comp("hello", "edabit")) # False

print(len("dbi"))

def is_even(n):
	return n % 2 == 0


def odd_or_even(word):
        return len(word) % 2 ==0


print(odd_or_even("apples")) # True
# The word "apples" has 6 characters.
# 6 is an even number, so the program outputs True.

print(odd_or_even("pears")) # False
# "pears" has 5 letters, and 5 is odd.
# Therefore the program outputs False.

odd_or_even("cherry") # True

def flip_bool(b):
        if b  == True:
                return 0
        elif b  == False:
                return 1
        elif b  == 1:
                return 0
        else:
                return 1


print(flip_bool(True)) # 0

flip_bool(False) # 1

flip_bool(1) # 0

flip_bool(0) # 1


def int_within_bounds(n, lower, upper):
        if n  >= lower and n < upper and type(n) == int:
                return True
        else:
                return False
        
                


print(int_within_bounds(3, 1, 9)) # True

print(int_within_bounds(6, 1, 6)) # False

print(int_within_bounds(4.5, 3, 8)) # False

print(int_within_bounds(0, 0, 1))

print(int_within_bounds(7, 7, 12))