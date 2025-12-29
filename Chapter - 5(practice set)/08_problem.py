# 8. If languages of two friends are same; what will happen to the program in problem 6 ?


d = {}

name = input("Enter friends name: ")
lang = input("Enter the language name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter the language name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter the language name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter the language name: ")
d.update({name : lang})

print(d)

# It will print the dictionary as it is because value can be same its not an issue
