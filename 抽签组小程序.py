# -*- coding: utf-8 -*-
counter=0  #计数器让第几组看的更明显
import random #引入random库
studentsnumber=[] #学号列表
for i in range (1,50) :  #用循环把学号填充到列表里
    studentsnumber.append(i)
random.shuffle(studentsnumber) #把列表中的数据打乱
while len(studentsnumber) > 4 : #咱们班49个人 肯定有一个组是四个人的
    counter+=1
    print("group {} ".format(counter),studentsnumber[0:3]) #把一组人输出
    for j in studentsnumber[0:3] : #把刚才输出的一组人从列表中除去
        studentsnumber.remove(j)
counter+=1
print("group {} ".format(counter),studentsnumber) #学号列表中只有这4个人了输出就行。