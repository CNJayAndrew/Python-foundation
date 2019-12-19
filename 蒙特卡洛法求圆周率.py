# 蒙特卡罗法 
# 随机数来20000个，计算PI
import random
x = []
y = []

n = 50000000
for i in range(n):
    x.append( random.random() )
    y.append( random.random() )

count = 0
  
for i in range(n):
    # 计算该点（x[i],y[i]) 到（0.5，0.5）的距离 随机生成的都是在0-1之间的小数，所以应该是四分之一个圆。
    d = ( (x[i]-0.5)**2 + (y[i]-0.5)**2 )**0.5
    if d<= 0.5:
        count += 1
# count / n = pi*0.5*0.5 / 1
pi = count/n*4
print(pi )