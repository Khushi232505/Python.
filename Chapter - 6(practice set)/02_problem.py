'''Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.'''

maths = int(input("enter the marks of maths: "))
hindi = int(input("enter the marks of hindi: "))
english = int(input("enter the marks of english: "))

total_percentage = (100*(maths+hindi+english))/300

if(total_percentage >= 40 and maths >= 33 and hindi >= 33 and english >= 33):
    print("you passed ", total_percentage)
else:
    print("you failde try again next year", total_percentage)
