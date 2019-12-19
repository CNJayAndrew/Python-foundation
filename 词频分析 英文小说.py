a=open('d:/python/hlwe.txt','r') #打开文件
b=a.read()  #读文本文件
c=b.lower() #让文本中的单词都变成小写
d=c.split() #根据空格把单词切片，储存为一个序列
counts={} #创建一个字典
for words in d :   #让切片之后的元素的值在循环中赋予words
        if words in counts : #如果在这个字典中的话，值加一
                counts[words]=counts[words]+1
        else : #否则将该元素作为键加入字典，值赋值为一
                counts[words]=1
e=list(counts.items()) #字典无法排序，将其转换为列表
e.sort(key=lambda x:x[1],reverse=True) #排序
print(e)
for i in e : #寻找前100个。
    sum=0
    print (i)
    sum+=1
    if sum==100 :
            break
a.close()