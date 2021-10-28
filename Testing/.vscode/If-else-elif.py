'''n = int(input('Enter Number: '))
if n % 2 == 0:
    print("%d is even"%n)
else:
    print("%d odd is"%n)'''

'''n = int(input('Enter Number: '))
if n % 2 == 0:
    print("%d is even"%n)
elif n % 2 != 0:
    print("%d odd is"%n)'''

'''salary = int(input("Enter Your Salary :"))
if salary >= 15000:
    if salary < 70000:
        print("Silver Card")
    elif salary < 100000:
        print("Golden Card")
    elif salary >= 100000:
        print("Platinum Card")
else:
    print("Sorry you can't make a credit card.")'''

m = int(input("Mount :"))
d = int(input("Day :"))

if m % 3 == 0:
    if d < 21:
        if m == 1 or m == 2 or m == 3:
            print("Winter")
        elif m == 4 or m == 5 or m == 6:
            print("Spring")
        elif m == 7 or m == 8 or m == 9:
            print("Summer")
        elif m == 10 or m == 11 or m == 12:
            print("Fall")
    else :
        if m == 1 or m == 2 or m == 3:
            print("Spring")
        elif m == 4 or m == 5 or m == 6:
            print("Summer")
        elif m == 7 or m == 8 or m == 9:
            print("Fall")
        elif m == 10 or m == 11 or m == 12:
            print("Winter") 
else:
    if m == 1 or m == 2 or m == 3:
        print("Winter")
    elif m == 4 or m == 5 or m == 6:
        print("Spring")
    elif m == 7 or m == 8 or m == 9:
        print("Summer")
    elif m == 10 or m == 11 or m == 12:
        print("Fall")