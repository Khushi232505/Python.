friends = ["Apple", "Orange", 5, 345.06, False,  "Aakash", "Rohan"]
print(friends[0])

# Append Method
friends.append("Khushi")
print(friends)

# Sort Method
number = [7,4,9,6,2,0,1]
number.sort()
print(number)

# Reverse Method
number.reverse()
print(number)

# Insert Method
number.insert(4,12) # Insert 12 such that its index in the list is 4
print(number)

#Pop Method(deleting an element)
print(number.pop(3))
number.pop(4)
print(number)

#Remove Method
number.remove(6)
print(number)
