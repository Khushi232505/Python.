marks ={
    "Harry": 100,
    "Khushi":50,
    "Rohan": 23,
    0: "Yuvraj"
}

print(marks.items()) #Returns a view object of (key, value) pairs.

print(marks.keys())  # Returns a list containing dictionary's keys

print(marks.values()) # Returns a list containing dictionary's values

marks.update({"Harry":90, "Renuka": 78}) # Updates the dictionary with supplied key-value pairs.
print(marks)

print(marks.get("Khushi2")) #Prints None
print(marks["Khushi2"]) # Returns and error

marks.clear() # Removes all items from the dictionary.
print(marks)

marks.pop("Rohan") # Removes and returns the value for the given key. If key not found, returns default
print(marks)  

print(marks.popitem())
# Removes and returns the last inserted (key, value) pair as a tuple.
