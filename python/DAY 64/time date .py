# for hourss



# from datetime import date

# d=date(2026,4,17)
# print(d)


# from datetime import time
# t=time(7,22)

# print(t)



'date formates'

# from datetime import datetime

# t=datetime.now().strftime("%d:%m:%B:%Y")
# print(t)
'only time'

# from datetime import datetime
# t=datetime.now().strftime("%I:%M:%p")
# print(t)

"birthday" #ad and remove date
# from datetime import datetime,timedelta
# today_late=datetime.now().date()
# # print(today_late)
# after=today_late+timedelta(days=10)
# print(after)


'time'
# from datetime import datetime,timedelta

# t=datetime.now()
# after=t+timedelta(minutes=19)
# print(after)

# from datetime import datetime

# t1="13:30"

# t=datetime.strptime(t1,"%H:%M")
# t_12=t.strftime("%I:%M:%p")
# print(t_12)




# t2="1:30 pm"

# t4=datetime.strptime(t2,"%I:%M %p")
# t_13=t4.strftime("%H:%M:%p")
# print(t_13)

'tasssssssssssssssssssssk'
# from datetime import datetime,timedelta
# import pyttsx3
# engine=pyttsx3.init()
# alarm=datetime.now()
# alarm_t=alarm+timedelta(seconds=5)
# # print(alarm_t)
# while True:
#     now=datetime.now()
#     if now>=alarm_t:
#         engine.say("hey chuuthiya wake up")
#         engine.runAndWait()
#         break




'json module'

# java script object notation

# it is seen in dict format but its in string fromat

# use in api ,webb devop,datatransfer

# it is light weight format 


# dumps---when pusing into puthon file to json File








def patterns(m):
    for x in range(1,m+1):
        for y in range(1,m+1):
            if x==1 or y==1 or x==m or y==m:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

patterns(4)



