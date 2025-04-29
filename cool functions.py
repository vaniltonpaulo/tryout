
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
