
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






print(eda_bit(0, 10)) # ["EdaBit", 1, 2, "Eda", 4, "Bit", "Eda", 7, 8, "Eda", "Bit" ]

print(eda_bit(14, 20)) # [14,  "EdaBit", 16, 17,  "Eda", 19, "Bit" ]

print(eda_bit(99, 106)) # ["Eda", "Bit", 101, "Eda", 103, 104, "EdaBit", 106 ]

# Create a function that returns the mean of all digits.
# The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).


def mean(num):
     x = [int(x) for x in str(num)]
     result  = sum(x)/ len(x)
     return  int(result)


mean(42) #➞ 3

print(mean(12345)) #➞ 3

mean(666) #➞ 6


def square_digits(n):
    x = [int(digit) for digit in str(n)]     # split digits
    x = [i ** 2 for i in x]                  # square each digit
    x = [str(i) for i in x]                  # convert back to string
    result =  "".join(x)                     # join without spaces
    return int(result)                        



print(square_digits(9119)) # 811181

square_digits(2483) # 416649

square_digits(3212) # 9414

