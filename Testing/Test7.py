#No.14
'''n = int(input("Enter number: "))
a = n % 2 #คู่-คี่
character1 = str(input("Enter character1: "))
character2 = str(input("Enter character2: "))
output = (n // 2) * (character1 + character2) + (a * character1) #a have value = a * character1 but a don't have value a >> 0 (0 * charater1) = 0 
print(output)'''

#No.15
'''print("First fraction")
a = int(input())
b = int(input())
print("Second fraction")
c = int(input())
d = int(input())
sum1 = ((a*d)+(b*c)) 
sum2 = (b*d)
print("Summation of the teo fractions is %d / %d"%(sum1,sum2))'''

#No.16
'''s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
sum = s1 + s2
hour = sum // 3600 #60*60 second to hour
minute = (sum % 3600) // 60
seconds =  (sum % 3600) % 60
print("It is %d hours %d minutes and %d seconds."%(hour,minute,seconds))'''

