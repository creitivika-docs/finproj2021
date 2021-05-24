import time

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

print("Hello!")
answer=input("введите команду")
while True :
    if (answer=="calculating"):
        print("character")
        answer=input()
        if (answer=="+"):
            a=int(input("1 part"))
            b=int(input("2 part"))
            c=a+b
            print(str(c))
        
        if (answer=="-"):
            a=int(input("1 part"))
            b=int(input("2 part"))
            c=a-b
            print(str(c))
        
        if (answer=="*"):
            a=int(input("1 part"))
            b=int(input("2 part"))
            c=a*b
            print(str(c))
        
        if (answer=="/"):
            a=int(input("1 part"))
            b=int(input("2 part"))
            c=a/b
            print(str(c))
        
        if (answer=="root"):
            a=int(input("1 part"))
            b=int(input("2 part"))
            c=b**(1/a)
            print(str(c))
        
        if (answer=="power"):
            a=int(input("1 part"))
            b=int(input("2 part"))
            c=a**b
            print(str(c))
    if (answer=="talk"):
        answer=input()
        if (answer=="2009"):
            print("Hello_Creator")
        else :
            print("I don't care what you say.")
    if (answer=="file"):
       
       answer=input("comand")
       if (answer=="write"):
            f = open('yy.txt', 'a')
            r=input()
            
            f.close()
       if (answer=="read"):
            f = open('yy.txt', 'r')
            print(f.read())
            f.close()
       if (answer=="delete"):
            f = open('yy.txt', 'w')
           
            f.close()
    if (answer=="data"):
        answer=input()
        if (answer=="data"):
            print("Year:"+str(year)+" Month:"+str(month)+" Day:"+str(day))
        if (answer=="time"):
            print("time: "+str(hour)+":"+str(minute))
            
    answer=input("введите команду")
