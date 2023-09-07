
'''
a=(2+100)\
   **3\
   *50\
   /4
print(a)
'''
'''
m=int(input())

fare=70+30*(m-1)
print(fare)
'''
'''
numapple=100
numstu=23
print('吃到第' , numapple//numstu , '天')
print('第',numapple//numstu+1,'天會不夠吃')
print('缺',numstu-(numapple%numstu),'幾顆')
'''
'''
a=round(28.1449,2)

b=round(28.145,2)

c=round(28.1451,2)
print(a)
print(b)
print(c)

'''
'''
y=5.44E-1
print(y)
y=5.44E-2
print(y)
y=5.44E-3
print(y)
y=5.44E-4
print(y)
y=5.44E-5
print(y)
'''
'''
xt=True
x=1+xt
print(x)
print(type(x))

yt=False
x=1+yt
print(x)
print(type(x))
'''
#a='''I belie
#ve i 
#can fly'''
#print(a)
'''
a='I belie\
ve i\
can fly'
print(a)
a=('I belie'+
've i'+
'can fly')
print(a)
'''
'''
ste=('I can\'t stop')
print(ste)
ste=('I can\t stop')
print(ste)
ste=('I can\b\b stop')
print(ste)
'''
'''
num=int(input('input a number'))
print(num*3)
print(str(num)*3)
'''
'''
v=1225
distance=384400
sum=distance//v
print(sum//24,'days',sum%24,'hours')
'''
'''
x1=1 x2=2 y1=3 y2=4
dist=((x1-x2)**2+(y1-y2)**2)**0.5    #**0.5是開根號
'''
'''
x1=float(input('請輸入x1:'))
y1=float(input('請輸入y1:'))
x2=float(input('請輸入x2:'))
y2=float(input('請輸入y2:'))
dist=abs(x1-x2)+abs(y1-y2)
print(dist)
'''
'''
x1=float(input('請輸入上底:'))
y1=float(input('請輸入下底:'))
h=float(input('請輸入高:'))
print('梯形面積為:',(x1+y1)*h/2)
'''
'''
a='sss'
b='ttt'
c='fff'
print(a,b,c,sep=',')
print(a,b,c,sep='    ')
print(a,b,c,sep='\n')
'''
'''
a='joe'
b=3.0
c='apple'
print('%s likes to each %s %s a week'%(a,b,c))
'''
'''
name1='joe'
name2='terry'
scores1=93.145
scores2=33.7
print('%-6s %5.3f'%(name1,scores1))     #%後面數字5為整個字串長度，向左對齊，不夠左邊補空位
print('%-6s %5.3f'%(name2,scores2))     #小數點後數字表示小數點後幾位，不夠右方補0，太少四捨五入
'''

word=input()
word=word.lower()
print(word)
























