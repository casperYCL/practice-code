#老師
#1
'''
x=list(input())
x.reverse()
for i in range(len(x)):
    print(x[i],end='')
print()
'''
#2
'''
import random
seed=int(input())
random.seed(seed)
x=[]
ans=[]
for i in range(1,43):
    x.append(i)
for i in range(6):
    ran=random.randint(1,42-i)
    ans.append(x[ran])
    x.remove(x[ran])
for i in range(6):
    print(ans[i],end='\t')
print()


'''
#3
'''
row1=list(map(int,input().split()))
row2=list(map(int,input().split()))     
row3=list(map(int,input().split()))
row4=list(map(int,input().split()))
row5=list(map(int,input().split()))

mat=[row1,row2,row3,row4,row5]
for i in range(7):
    for j in range(4):
        print(mat[j][i],end='\t')
    print(mat[4][i])
'''
#4
'''
def F(h,w):
    for i in range(1,h+1):
        for j in range(1,w+1):
            print(i*j,end='\t')
        print()

x,y=map(int,input().split())
F(y,x)
'''
#5
'''
def C(x):
    num=1
    for i in range(1,x+1):
        num=num*i
    return num

a,b=map(int,input().split())
sum=C(a)/(C(b)*C(a-b))
print(int(sum))
'''
#6
'''
def digit(x):
    for i in range(len(x)-1):        
        print(x[i],end=' ')
    print(x[len(x)-1])
x=list(input())
digit(x)
'''
#7
'''
x=int(input())
row=[]
for i in range(x):
    num=int(input())
    row.append(num)
row.sort()
for i in range(x):
    print(row[i])
'''
#8
'''
def arr(x):
    for i in range(len(x)):

        x[i]=x[i]**2
    for i in range(len(x)-1):
        
        print(x[i],end='\t')
    print(x[len(x)-1])

x=list(map(int,input().split(' ')))
arr(x)
'''
#9
'''
num=list(map(int,input().split()))
time=len(num)-1
for j in range(time):    
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            x=num[i]
            num[i]=num[i+1]
            num[i+1]=x
for i in range(len(num)-1):
    print(num[i],end=' ')
print(num[len(num)-1])
'''
#10
'''
num=list(map(int,input().split()))
time=len(num)-1
max1=num[0]*num[1]
for i in range(time):
    for j in range(i,len(num)-1):
        now=num[j]*num[j+1]
        if now>max1:
            max1=now
print(max1)
'''
#11
'''
num=list(map(int,input().split()))
for i in range(len(num)):
    for j in range(i,len(num)):           
        list1=num[i:j+1]
        sum1=sum(list1)
        if sum1==0:
            ans=num[i:j+1]
            for k in range(len(ans)):
                print(ans[k],end=' ')
            print()
            break
'''
#12
'''
f=list(map(int,input().split()))
g=list(map(int,input().split()))
f=sorted(f)
g=sorted(g)
re=[]
sam=0
ans=0
for i in range(len(f)):
    for j in range(len(g)):
        if f[i]==g[j]:
            sam+=1
            re.append(g[j])
    if sam>=1:
        ans+=1
        sam=0
        for k in range(len(re)):
            g.remove(re[k])
        re=[]
print(ans) 
'''        
# num1=list(map(int,input().split()))
# num2=list(map(int,input().split()))
# set1=set()
# for i in range(len(num1)):
#     if num1[i] not in set1:
#         set1.add(num1[i])

# count=0
# set2=set()
# for i in range(len(num2)):
#     if num2[i] in set1 and num2[i] not in set2:
#         set2.add(num2[i])
#         count+=1
        
# print(count)
#14
'''
x=int(input())
num=[]
cur=1
for i in range(x):
    if i%x==0:
        sub=[j for j in range(cur,cur+x)]
        num.append(sub)
        cur+=x
    else:
        sub=[j for j in range(cur+x-1,cur-1,-1)]
        num.append(sub)
        cur+=x
for i in range(x):
    for j in range(len(num)):
        print(num[i][j],end='\t')
    print()
print()
for i in range(x):       
    for j in range(len(num)):
        print(num[j][i],end='\t')
    print()
'''
#助教
#1
'''
x=list(input())
x.reverse()
for i in range(len(x)):
    print(x[i],end='')
print()
'''
#2
'''
import random
seed=int(input())
random.seed(seed)
num=[]
ans=[]
for i in range(1,43):
    num.append(i)
for i in range(6):
    ran=random.randint(1,43-i)
    take=num[ran]
    ans.append(take)
    num.remove(num[ran])
for i in range(6):
    print(ans[i],end='\t')
print()
'''
#3
'''
def F(w,h):
    for i in range(1,h+1):
        for j in range(1,w+1):
            print(i*j,end='\t')
        print()

weight,height=map(int,input().split())
F(weight,height)
'''
#4
'''
def C(x):
    a=1
    for i in range(1,x+1):
        a=a*i
    return a

m,n=map(int,input().split())
ans=C(m)/(C(n)*C(m-n))
print(int(ans))
'''
#5
'''
def sep(nums):
    nums=list(nums)
    for i in range(len(nums)):
        print(nums[i],end=' ')
print()

num=input()
sep(num)
'''
#7
'''
def arr(lst):
    for i in range(len(lst)):
        lst[i]=lst[i]**2
    for j in range(len(lst)):
        print(lst[j],end='\t')
    print()

x=list(map(int,input().split()))
arr(x)
'''
#8
'''
def bouble(x):
    for i in range(len(x)):
        tmp=0
        for j in range(i,len(x)):
            if x[j]<x[i]:
                tmp=x[i]
                x[i]=x[j]
                x[j]=tmp
    for k in range(len(x)):
        print(x[k],end='\t')
    print()

num=list(map(int,input().split()))
bouble(num)
'''
#9
'''
def arr(num):
    sum=[]
    max1=0
    for i in range(len(num)-1):
        a=num[i]*num[i+1]
        sum.append(a)
    max1=max(sum)
    print(max1)

x=list(map(int,input().split()))
arr(x)
'''
#10
'''
def f(n):
   if n==1:
       return n+1
   else:
       return f(n-1)+f(n//2) 

x=int(input())
print(f(x))
'''
#11
'''
def res(num):           
    num1=num[::-1]
    if num==num1:
        print('Yes')
    else:
        print('No')

x=input()
res(x)
'''

