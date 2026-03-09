'''modules
random.random ---random numbers 0ton
random.random int ===betw num
random.randname --between number but with step
random.uniform ---for float ---
choice ----only one char at a time  //so we have to use loop
choices = k times we can give
sample ---- only use string len  //so we can not give more than len of string 

range
ex1-
passwors sum
'''
# import random
# a =int(input("enter no/of alpha:-"))
# b =int(input("enter no/of number:-"))
# c =int(input("enter no/of spl symbols:-"))
# password=" "
# for x in range(a):
#     d= random.choice("abcdefghijklmnopqrstuvwxyz")
#     password+=d
# for j in range(b):
#     d2 =random.choice("1234567890")
#     password+=d2
# for m in range(c):
#     d3=random.choice("@#$!%&*")
#     password+=d3
# print(password)


# import random
# password=""
# a =int(input("enter no/of alpha:-"))
# b =int(input("enter no/of number:-"))
# c =int(input("enter no/of spl symbols:-"))
# l=[]
# l+=(random.choices("qwertyuiopasdfghjklzxcvbnm",k=a))
# l+=(random.choices("1234567890",k=b))
# l+=(random.choices("!@#$%^&*()_+",k=c))
# for i in l:
#     password+=i

# print(password)


"sample"

# import random
# print(random.sample("samer",k=5))


"THIRD PARTY"


# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello")
# engine.runAndWait()


import pyttsx3
import time
en = pyttsx3.init()
en.setProperty('rate',50)

voices = en.getProperty('voices')
en.setProperty('voice',voices[0].id)
en.say('hi')
en.runAndWait()


# l = ['vinay','raj','mohan']
# for x in l:
#   en.say(x)
#   time.sleep(3)
#   en.runAndWait()