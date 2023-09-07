#1
'''
mile=float(input())
print(f'{mile*1.6:.2f}')
'''
#2
'''
mile=float(input())
print(f'{mile*9/5+32:.2f}')
'''
#3
'''
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
'''
#4
'''
chinese=int(input())
math=int(input())
english=int(input())
sum=chinese+english+math
print(sum)
print(sum//3)
'''
#5
'''
high, weigh=input().split( )
print(float(high)/2.54)
print(float(weigh)/0.454)
'''
#6
'''
a, b = input().split() #將輸入字串用split()切開
c = a.split(b)
for i in c:
  print(i)
'''
#7
'''
word=input()
word=word.lower()
print(word)
'''
#8
'''
a=float(input())
print(f"{a*0.26184:.1f}")
'''
#9

# a=float(input())
# print(f"{a/600:.1f}")

#10

# string = input()
# a=input()
# b=input()
# string=string.replace(a,b)
# print(string)

#11

# sec=int(input())
# a=(sec+7000)//1000%10
# b=(sec+700)//100%10
# c=(sec+70)//10%10
# d=(sec+7)%10
# print(c,d,a,b,sep='')


sec=int(input())
a=sec//1000
b=sec//100
c=sec//10
d=sec//1

a=(a+7)%10
b=(b+7)%10
c=(c+7)%10
d=(d+7)%10

print(f"{c}{d}{a}{b}")


#12

# a=int(input())
# b=int(input())
# print(f'{a}+{b}={a+b}')
# print(f'{a}*{b}={a*b}')
# print(f'{a}-{b}={a-b}')
# print(f'{a}/{b}={a//b}...{a%b}')

#13

# a=input()
# print(ord(a))

#14
# a=input()
# a=ord(a)
# print(f'{a:x}')#b 2進位 #o 8進位 #x 16進位

#15

# a=input()
# a=int(a,16)
# a=chr(a)
# print(f'{a}')

#16

# import math
# r, h=input().split()
# v=(float(r)**2)*float(h)*math.pi
# print(v)

# import math
# paras = input().split() 
# r = float(paras[0])
# h = float(paras[1])
# vol = math.pi * r**2 * h
# print(f"{vol}")






