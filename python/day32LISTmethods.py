"find prime numbers in list"

s = [10,11,2,3,4,5,3]
for num in range(len(s)):
    if s[num]>1:
        count=0
        for i in range(2,s[num]+1):
            if s[num] % i == 0:
                count+=1
                break
        if count==1:
            print(s[num],"its a prime number")
        else:
            print(s[num],"not a prime")