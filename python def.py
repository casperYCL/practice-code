#def
'''
def sayhi(name,title='先生',hi='你好'):
    print(name,title,hi,sep='')
sayhi('王曉明',hi='好久不見')
'''
'''
def calc(w,h,d=1):
    return w*h*d
print(calc(3,4))
print(calc(3,4,5))
'''
'''
def calc(w,h):
    if(w<=0 or h<=0):
        return
    return w*h
print(calc(-4,5))
print(calc(4,5))#回傳質是tuple
'''
'''
def calc(w,h):
    return [((w+h)*2,w*h),'正方形' if w==h else '長方形']
print(calc(1,1))
print(calc(4,5))
'''
'''
s=[(3,4),(5,6),(7,8)]
def calc(w,h):
    return w*h
def calcall(conta,func):
    for i in conta:
        print(func(i[0],i[1]),end=' ')
calcall(s,calc)


s=[(3,4),(5,6),(7,8)]
def calcall(conta,func):
    for i in conta:
        print(func(i[0],i[1]),end=' ')
calcall(s,lambda w,h:w*h)        #lambda 匿名函式
calcall(s,lambda w,h:(w+h)/2)
'''
'''
s=[(3,4),(2,2),(5,3)]
print(sorted(s,key=lambda e:e[1]))    #用每個list的1號大小來排
'''
'''
def prnsum(name,pre='>',*args,post='#'):
    print(name,pre,args,'=',sum(args),post)
prnsum('加總',':',1,2,3,4,post='元')
'''
'''
def prnprice(name,**kwargs):    #*跟**是打包函數
    print(name,kwargs)
prnprice('飲料',紅茶=40,咖啡=70,果汁=85)
'''
'''
def prnprice(name,*args,**kwargs):
    print(name,args,':',kwargs,sep='')
dscnt=('早餐8折','消夜9折')
drink={'紅茶':40,'咖啡':70,'果汁':85}
prnprice('飲料',*dscnt,**drink)
'''
'''
a=b=c=1
def test(b):
    a=2
    print(a,b,c)
test(3)
print(a,b,c)
'''
'''
a=b=c=1
def test(b):
    global c
    a=2
    c=33
    print(a,b,c)
test(3)
print(a,b,c)
'''
'''
s=[1,2,3]
t=[4,5,6]
def test(a):
    a[0]='aaa'   #a是區域變數改變了全域變數串列s
    t[0]='ttt'
    s=[7,8,9]     #s是區域變數
    s[0]='sss'
    print(a,t)
test(s)
print(s,t)       #s['aaa',2,3]
'''







