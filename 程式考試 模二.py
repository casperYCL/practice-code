#1
'''
x=int(input())
if x<-1:
    ans=3*x*x
elif x>1:
    ans=(2*x)+3
else:
    ans=x**3+3*x-3
print(ans)
'''
#2
'''
heigh,bg=input().split()
heigh=int(heigh)
bg=int(bg)
if bg==1:
    weight=(heigh-80)*0.7
else:
    weight=(heigh-70)*0.6
print(round(weight,1))
'''
#3
'''
money,x,y,z=input().split()
money=int(money)
x=int(x)
y=int(y)
z=int(z)
sum=x*15+y*20+z*30
money=money-sum
x50=money//50
x5=(money-50*x50)//5
x1=money-50*x50-5*x5
print(x1)
print(x5)
print(x50)
'''
#4
'''
x,y=input().split()
x=int(x)
y=int(y)
z=x**2+y**2
z1=100**2
if z<z1:
    print('inside')
else:
    print('outside')
'''
'''
x,y=input().split()
x=int(x)
y=int(y)
z=(x-3)**2+(x-4)**2
z1=100**2
if z<=z1:
    print('inside')
else:
    print('outside')
'''
#5#
'''
x1,y1=input().split()
x2,y2=input().split()
x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)
x=x1*60+y1
y=x2*60+y2
if x>y:
    min=1440-x+y
else:
    min=y-x
if min<=30:
    print(0)
elif min<=120:
    price=(min//30)*30
elif 120<min<=240:
    price=((min-120)//30)*40+120
else:
    price=((min-240)//30)*60+120+160
print(price)
'''
#6
'''
month=int(input())
if 3<=month<=5:
    print('Spring')
elif 6<=month<=8:
    print('Summer')
elif 9<=month<=11:
    print('Autumn')
else:
    print('Winter')
'''
#7
''' 
m,d=input().split()
m=int(m)
d=int(d)
if m==1:
    if 1<=d<=20:
        print('Capricorn')
    if 21<=d<=31:
        print('Aquarius')
elif m==2:
     if 1<=d<=18:
        print('Aquarius')
     if 19<=d<=28:
        print('Pisces')
elif m==3:
     if 1<=d<=20:
        print('Pisces')
     if 21<=d<=31:
        print('Aries')
elif m==4:
     if 1<=d<=20:
        print('Aries')
     if 21<=d<=30  :
        print('Taurus')
elif m==5:
     if 1<=d<=21:
        print('Taurus')
     if 22<=d<=31:
        print('Gemini')
elif m==6:
     if 1<=d<=21:
        print('Gemini')
     if 22<=d<=30:
        print('Cancer') 
elif m==7:
     if 1<=d<=22:
        print('Cancer')
     if 23<=d<=31:
        print('Leo')
elif m==8:
     if 1<=d<=23:
        print('Leo')
     if 24<=d<=31:
        print('Virgo')
elif m==9:
     if 1<=d<=23:
        print('Virgo')
     if 24<=d<=30:
        print('Libra')
elif m==10:
     if 1<=d<=23:
        print('Libra')
     if 24<=d<=31:
        print('Scorpio')
elif m==11:
     if 1<=d<=22:
        print('Scorpio')
     if 22<=d<=30:
        print('Sagittarius')
elif m==12:
     if 1<=d<=22:
        print('Sagittarius')
     if 22<=d<=31:
        print('Capricorn')
'''
#8
'''
year=int(input())
if year%400==0:
    if year%100==0:
        if year%4==0:
            print('Leap Year')
        else:
            print('Common Year')
    else:
        print('Common Year')
else:
    print('Common Year')
'''
#9
'''
x=int(input())
if x<=120:
    price1=x*2.1
    price2=x*2.1
elif 120<x<=330:
    price1=(x-120)*3.02+(120*2.1)
    price2=(x-120)*2.68+(120*2.1)
elif 330<x<=500:
    price1=(x-330)*4.39+(120*2.1)+(330-120)*3.02
    price2=(x-330)*3.61+(120*2.1)+(330-120)*2.68
elif 500<x<=700:
    price1=(x-500)*4.97+(120*2.1)+(330-120)*3.02+(500-330)*4.39
    price2=(x-500)*4.01+(120*2.1)+(330-120)*2.68+(500-330)*3.61
else:
    price1=(x-700)*5.63+(120*2.1)+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97
    price2=(x-700)*4.50+(120*2.1)+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01
print(round(price1,2))
print(round(price2,2))
'''
#10
'''
x=input()
if ord(x)<ord('a'):
    print(x.lower())
else:
    print(x.upper())
'''
#11
'''
x=int(input())
if x%2==0:
    print('Even')
else:
    print('Odd')
'''
#12
'''
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if c>b and c>a :
    if a+b>c and a+c>b and b+c>a:
        print('True')
        
    else:
        print('False')
else:
    print('False')
'''
#13
'''
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if (a**2+b**2)<c**2:
    print('Obtuse triangle')
elif (a**2+b**2)==c**2:
    print('Right triangle')
else:
    print('Acute triangle')
'''
#14
'''
x1,x2,x3,x4,x5=input().split()
x1=float(x1)
x2=float(x2)
x3=float(x3)
x4=float(x4)
x5=float(x5)
list1=[x1,x2,x3,x4,x5]
max1=max(list1)
min1=min(list1)
max1=float(max1)
min1=float(min1)
print(f'{max1:.2f}')
print(f'{min1:.2f}')
'''
#15
'''
# *
# **
# ***
h=int(input())
for i in range(1,h+1):
    for j in range(1,i+1):
        print('*',end='')
    print()        
'''
'''
x=int(input())
for i in range(1,x+1):
    print('*'*(i),end='')
    print()
'''
'''
x=int(input())
i=1
while x+1>i:
    print('*'*i)
    i+=1
'''
'''
# ***
# **
# *
h=int(input())
for i in range(h,0,-1):
    for j in range(i,0,-1):
        print('*',end='')
    print()
'''
'''
x=int(input())
for i in range(x):
    print('*'*(x-i),end='')
    print()
'''
'''
# ***
#  **
#   *
h=int(input())
for i in range(0,h):
    for j in range(i,0,-1):
        print(' ',end='')
    print('*'*(h-i))
'''
'''
x=int(input())
for i in range(x):
    print(' '*(i),end='')
    print('*'*(x-i),end='')
    print()
'''
'''
#   *
#  **
# ***
h=int(input())
for i in range(h,0,-1):
    for j in range(i-1,0,-1):
        print(' ',end='')
    print('*'*(h-i+1))
'''
'''
x=int(input())
for i in range(x):
    print(' '*(x-i-1),end='')
    print('*'*(i+1),end='')
    print()
'''
'''
h=int(input())
for i in range(h,0,-1):
    for j in range(i-1,0,-1):
        print('*',end='')
    for j in range(h+1,i,-1):
        print(j-i,end='')
    print()
'''
'''
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
x=int(input())
for i in range(1,x+1):
    print(' '*(x-i),end='')
    print('*'*(2*i-1),end='')
    print()
for i in range(x-1,0,-1):
    print(' '*(x-i),end='')
    print('*'*(2*i-1),end='')
    print()
'''
#18
'''
x=int(input())
a=False
for i in range(2,x):
    if x%i==0:
        a=True
        break
if a==True:
    print('No')
else:
    print('Yes')
'''
#19#
'''
t=int(input())
for i in range(t):
    x1,x2,x3=input().split()
    x1=int(x1)
    x2=int(x2)
    x3=int(x3)
    if x1>=60 and x2>=60 and x3>=60:
        print('P')
    elif x1<60 and x2>=60 and x3>=60:
        sum=x1+x2+x3
        if sum>=220:
            print('P')
        else:
            print('M')
    elif x1>=60 and x2<60 and x3>=60:
        sum=x1+x2+x3
        if sum>=220:
            print('P')
        else:
            print('M')
    elif x1>=60 and x2>=60 and x3<60:
        sum=x1+x2+x3
        if sum>=220:
            print('P')
        else:
            print('M')
    elif x1>=80 and x2<60 and x3<60:
            print('M')
    elif x1<60 and x2>=80 and x3<60:
            print('M')    
    elif x1<60 and x2<60 and x3>=80:
            print('M')
    else:
            print('F')
'''
#20
'''
x=int(input())
sum=0
for i in range (1,x+1):
    if i%3==0:
        sum+=i
print(sum)
'''
#21
'''
x,y=input().split()
x=int(x)
y=int(y)
gcd=0
lcm=0
for i in range (max(x,y)-1,0,-1):
    if x%i==0 and y%i==0:
        gcd=i
        break
for i in range (max(x,y)+1,x*y+1):
    if i%x==0 and i%y==0:
        lcm=i
        break
print(gcd)
print(lcm)
'''
#22
'''
x=int(input())
for i in range (1,x+1):
    for j in range (1,x+1):
        print(i*j,end="\t")
    print()
'''
#23
'''
x=int(input())
for i in range (1,x+1):
    if x%i==0:
        print(i)
'''
#24#
'''
x=input()
num=x[0]
y=x[1]
num=int(num)
for i in range (1,num+1):
    print(y*num,end='')
    print()
'''
#25
'''
x=int(input())
sum=1
for i in range (1,x+1):
    sum=sum*i
print(sum)
'''
#26
'''
x=int(input())
sum=0
for i in range (1,x+1):
    sum+=i*(i+1)
print(sum)       
'''
#27
'''
x=int(input())
sum=0
for i in range (1,2*x,2):
    sum+=1/(i*(i+1))
print(sum) 
'''
#28
'''
x=int(input())
sum=0
for i in range (1,x+1):
    sum+=2**i
print(sum) 
'''
#29
'''
x=input()
list1=list(x)
t=0
sum=0
big=1
while int(x)>=big:
    sum+=int(x[t])
    t+=1
    big*=10
print(t)
print(sum)
'''
#30
'''
x=int(input())
y=0
for i in range (2,x):
    y=0
    for j in range (2,i):
        if i%j==0:            
            y+=1
            # print(y)
    if y==0:
        print(i)
'''
#31
''' 
x=int(input())
sum=1
y=0
for i in range (1,x+1):
    sum=sum*i
list1=list(str(sum))
for i in range (len(list1)-1,0,-1):
    if int(list1[i])==0:
        y+=1
    else:
        break
print(y)
'''
#32
'''
x=input()
list1=list(x)
list1.reverse()
# str1=''.join(list1)
# print(str1)
for i in range (len(list1)):
    print(list1[i],end='')
print()
'''
#33
'''
x=int(input())
a=True
i=0
sum=0   
while a==True:         
    if sum+i+1>x:
        a=False
    else:
        i+=1
        sum+=i
print(i)
'''
'''
x = int(input())
i = 1
sum = 1
while sum<x:
    i = i +1
    sum = sum+i
if sum>x:
    i = i-1
print(i)
'''
#34
'''
x=int(input())
sum=1
print(x)
for i in range(x):
    if sum<x:
        sum+=i
        print(sum,end='\t')
print()
for i in range(1,x+2):
    for j in range(1,i+1):        
            print(i,end='\t') 
'''
#35
'''
x=int(input())
for i in range(2,x//2):
    for j in range(i,x//2):
        for k in range(j,x//2):
            if i**2+j**2==k**2:
                print(i,j,k,sep='\t')
                print()
'''







