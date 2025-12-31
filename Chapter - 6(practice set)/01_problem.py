a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
d = int(input("Enter the fourth number : "))

if (a>b and a>c and a>d):
    print("Greatest number is a: ", a)
    
elif (b>a and b>c and b>d):
    print ("Greatest number is b: ", b)
    
elif (c>a and c>b and c>d):
    print("Greatest number is d: ", c)
    
else:
    print("Greatest number is d: ", d)
    

