import numpy as np
def ranflote(num):
    a=np.random.randn(num)
    mean1=np.mean(a)
    std1=np.std(a)
    print('float數量',num)
    print(mean1)
    print(std1)

a=ranflote(5)
a=ranflote(20)
a=ranflote(300)

'''
randn是以0為平均，1為標準差來分布的隨機值，所以做越多次平均數會越接近0，標準差也會越接近1，
但300次是最穩定，平均不會偏離0太多，標準差不會跟1差太多，5次和20次因為是常態分佈髓已也可能做出很接近0跟1的，
但不會每次都這麼接近數值變動較大，需要一定的次數才能維持平均和標準差的穩定，
'''