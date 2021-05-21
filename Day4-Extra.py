#If the number is a multiple of 4, print out a different message

print("This program will help you to divide")
num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num , "is an even number")
else:
    print(num , "is an odd number")

if num % check ==0:
    print(num , "completely divides by" , check)
else:
    print(num , "does not completely divides by" , check)
