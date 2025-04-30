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

get_discounts([100], "45%") # [45]