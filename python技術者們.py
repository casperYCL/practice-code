'''
a=[1,2,3,4,9,5,10,0.2,56,30,100,99]
mylist=['c','r','n','a','g']
mylist.sort()

print(mylist)
'''
'''
a=[1,5,3,4,6,8,7,6,1,3,2,5,9]
x=a.pop()
print(x)
print(a)
'''
'''
z=divmod(11,4)
'''
'''
i=1
while True:
    if i==5:
        i+=1
        continue
    print(i, end=' ')
    i+=1
    if i==11:
        break
print('結束')    
'''
'''
secret=input('請輸入通關密語')
while True:
    if secret=='out':
        break
    elif  secret=='喵喵':
        print('恭喜你過關了')
        break
    else:
        print('不對喔')
        break
    
print('再見')
'''
'''
s=[0,1,2,3]
for i in s:
    print(i,end=" ")
'''
'''
d={'a':0,'b':1,'c':2,'d':3}
for i in d.values():
    print(i,end=" ")
print(' | ',end=" ")
for i in d.items():
    print(i,end=" ")
print(' ') 
print('-----------')

for i in d.items():
    print(i[0],i[1])
print('-----------')
for key,value in d.items():
    print(key,value)
'''
'''
a=[[1,2,3,4],[3,6,8,3],[5,6,8,4],[3,73,7,3]]
cut=0
for i in a:
    for t in i:
        if t==3:
            cut+=1
print('有',cut,'個3')
'''
'''
for i in range(1,10):
    for n in range(1,10):
        print(f'{n}x{i}={n*i:2d}',end=' ')
    print()
'''
'''
person={1:('王','意欽'),9:('林','偉丞'),7:('林','偉和')}
for person_id, (first_name,last_name) in person.items():
    print(str(person_id)+'號-'+first_name+last_name)
'''
'''
sports=('tennis','soccer','baseball')
print(list(enumerate(sports,6)))
print('------')
for i,sports in enumerate(sports):
    print(i,sports,end=' ')
'''
'''
drinks=('紅茶','綠茶','奶茶')
prices=('20','30','40')
match=('布丁','蛋糕','鬆餅','吐司')
for drinks,prices,match in zip(drinks,prices,match):
    print(drinks, prices ,'元,建議甜點', match)
'''
'''
print([i*i for i in range(1,6)])
print({i*i for i in range(1,6)})
print({i:i*i for i in range(1,6)})

a=(i*i for i in range(1,6))
print(type(a))
print(list(a))
print(tuple(a))

s=[i*i for i in range(1,11) if i%2==0]
print(s)

a_a=[[1,2,3],[4,5,6],[7,8,9]]
print([e2 for e1 in a_a for e2 in e1 if e2!=4])
'''
'''
x=0b1101
print(x)
'''
'''
x=-10
print(x)
print(abs(x))#abs絕對值
x=3
y=2
print(pow(x,y))#x的y次方
x=10.5
print(round(x))#四捨五入 最左數字奇數四捨五入，偶數五捨六入
print(round(1.5))#四捨五入
print(round(2.5))#五捨六入
print(round(1.5543225,2))#取小數後兩位
'''
'''
s='a'
try:
    s=int(s)
    print('錯誤')
except:
    print('正確')        
'''
'''
while True:
    s=input('100內除數')
    try:
        print('100除以',s,'=',100/float(s))
        break
    except ValueError as e:
        print('ValueError',e)
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('其他例外')
    print('Try again')
print('end')
'''
'''
while True:
    s=input('請輸入1到100的除數')
    try:
        i=100/float(s)
    except ValueError:
        print('發生ValueError例外')
    else:
            print('100除',s,'=',i)
            break
    finally:
        print('你輸入的是',s)
    print('進入下個迴圈')
print('程式結束')
'''
'''
a,b=2,3
print(f'{a}和{b}相乘的結果是{a*b:+5.1f}')
print(f'{"a":<3}|{"a":>3}{"a":^3}')#靠左靠右靠中
print(f'{0.98765:.3e}')#科學記號顯示，數字取小數後幾位
print(f'{0.98765:+2%}')#百分比顯示分數後2位
print(f'{42:d},{42:b},{42:#X}')#10進位2進位16進位
'''
'''
print('1+{}={}'.format(2,3))
print('{1}-1={0}'.format(2,3))
print('{b}-1={a}'.format(a=2,b=3))
print('{0[1]},{0[0]},{1[2]}'.format([3,4],[2,3,4]))
'''












