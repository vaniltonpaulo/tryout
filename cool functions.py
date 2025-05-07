
# Programmer Pete is trying to create a function that returns True if two lists share the same length and
# have identical numerical values at every index, otherwise, it will return False.

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



head, *tail = [1, 2, 3, 4]
print(tail)



# if not lst:

# This checks if the list is empty.

# In Python, an empty list ([]) is considered False, and a non-empty list is True.

# So not lst will be True if the list is empty.


def last_ind(lst):
    if not lst:
        return None
    else:
        return lst[-1]


print(last_ind([0, 4, 19, 34, 50, -9, 2])) # 2

print(last_ind("The quick brown fox jumped over the lazy dog")) # "g"

print(last_ind([])) # None


def get_vote_count(votes):
    return votes.get("upvotes") - votes.get("downvotes")


print(get_vote_count({ "upvotes": 13, "downvotes": 0 })) # 13

print(get_vote_count({ "upvotes": 2, "downvotes": 33 })) # -31

get_vote_count({ "upvotes": 132, "downvotes": 132 }) # 0



def all_truthy(*args):
    return all(args)

print(all_truthy(True, True, True)) # True

all_truthy(True, False, True) # False

all_truthy(5, 4, 3, 2, 1, 0) # False


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



# Using dict.fromkeys()
# Another simple way to remove duplicates while preserving the order of elements is by using dict.fromkeys(). Since Python 3.7, dictionaries maintain insertion order.




# Initialize a list with some duplicates
a = [1, 2, 3, 3, 4, 4, 5, 5]

# Use dict.fromkeys() to preserve order and remove duplicates
res = list(dict.fromkeys(a))

print(res)






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




#Remove spaces at the beginning and at the end of the string:

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")



#Remove ,.grt:

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)



animals = ['cat', 'dog', 'rabbit', 'horse']

# get the index of 'dog'
index = animals.index('dog')

print(index)

# Output: 1




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
    
#hi mate

x= 1223