' Write a program to check whether a given number is positive, negative, or zero.'
n=int(input("Enter number: "))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")



# 2. Write a program to check whether a given number is even or odd. 
n=int(input("Enter number: "))
if n%2==0:
    print("Even")
else:
    print("Odd")



# 3. Write a program to find the largest of two numbers using if-else. 
a=int(input("A: "))
b=int(input("B: "))
if a>b:
    print("A is largest")
else:
    print("B is largest")



# 4. Write a program to find the largest of three numbers using if-elif-else. 
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("A is largest")
elif b>c:
    print("B is largest")
else:
    print("C is largest")



# 5. Write a program to check whether a given year is a leap year or not. 
y=int(input("Year: "))
if y%400==0 or (y%4==0 and y%100!=0):
    print("Leap Year")
else:
    print("Not Leap")



# 6. Write a program to check whether a given number is divisible by both 5 and 11.
n=int(input())
if n%5==0 and n%11==0:
    print("Divisible")
else:
    print("Not Divisible")


# 7. Write a program to check whether a character is a vowel or consonant. 
ch=input()
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")



# 8. Write a program to check whether a given character is an alphabet, digit, or special character. 

ch=input()
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special")




# 9. Write a program to check whether a person is eligible to vote based on age.
age=int(input())
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")




# 10. Write a program to check whether a number is a multiple of 3 or 7. 
n=int(input())
if n%3==0 or n%7==0:
    print("Yes")
else:
    print("No")




# 11. Write a program to calculate grade based on marks using if-elif-else. 
m=int(input())
if m>=90:
    print("A")
elif m>=75:
    print("B")
elif m>=60:
    print("C")
elif m>=40:
    print("D")
else:
    print("Fail")



# 12. Write a program to check whether a number is a two-digit or three-digit number. 
n=abs(int(input()))
if n>=10 and n<=99:
    print("Two digit")
elif n>=100 and n<=999:
    print("Three digit")
else:
    print("Invalid")




# 13. Write a program to check whether a given number is divisible by 2, 3, or both.
n=int(input())
if n%2==0 and n%3==0:
    print("Both")
elif n%2==0:
    print("2")
elif n%3==0:
    print("3")
else:
    print("None")



# 14. Write a program to find the minimum of two numbers. 
a=int(input())
b=int(input())
if a<b:
    print("Minimum:",a)
else:
    print("Minimum:",b)



# 15. Write a program to check whether a number is a perfect square. 
n=int(input())
r=int(n**0.5)
if r*r==n:
    print("Perfect Square")
else:
    print("Not Perfect")


# 16. Write a program to check whether a given temperature is hot, cold, or normal.
t=int(input())
if t>30:
    print("Hot")
elif t<15:
    print("Cold")
else:
    print("Normal")



# 19. Write a program to calculate electricity bill using conditional statements.
u=int(input())
if u<=100:
    bill=u*1
elif u<=200:
    bill=100*1+(u-100)*2
else:
    bill=100*1+100*2+(u-200)*3
print("Bill =",bill)




'20. Write a program to check whether a number is within a given range.'
n=int(input())
if n>=10 and n<=50:
    print("In Range")
else:
    print("Out of Range")
