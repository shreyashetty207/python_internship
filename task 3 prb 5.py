#Write a Python program to remove the intersection of a 2nd set from the 1st set.
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print("Sets:")
print(a)
print(b)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
a.difference_update(b)
print(a)
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(a-b)
