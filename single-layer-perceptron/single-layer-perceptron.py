# -*- coding: utf-8 -*-
"""
Created on Tue May  1 15:41:13 2018

@author: Alex
"""
#假设平面坐标系上有三个点，（3,3）（3,4）这两个点的标签为1，（1,1）这个点的标签为-1.
#构建神经网络来分类

#由于要分类的是二维数据，所以只需要2个输入节点，可以将神经元的偏置值也设置成一个节点，
#这样就需要3个输入节点

#输入数据有3个（1,3,3），（1,4,3），（1,1,1）
#对应的标签为（1,1,-1）
#初始化权值w0，w1，w2,取-1到1的随机数
#学习率（learning rate设置为0.11）
#激活函数为sign函数

import numpy as np
import matplotlib.pyplot as plt

#输入数据（二维矩阵），每行是一组数据
X = np.array([[1,3,3],
              [1,4,3],
              [1,1,1]])

#三组数据对应的三个标签，期望的输出
Y = np.array([1,1,-1])
#权值初始化，1行3列，取值范围-1到1
W = (np.random.random(3)-0.5)*2
print(W)
#学习率设置
lr = 0.11
#计算迭代次数
n = 0
#神经网络输出
O = 0

def update(): #更新权值的函数
    global X,Y,W,lr,n #引言全局变量
    n+=1 #没更新一次n+1
    O = np.sign(np.dot(X,W.T))#.T表示转置，得到3元素列向量
#    W_C = lr*(Y-O.T).dot(X)#当数据组数较大时，权值将可能很大
    W_C = lr*(Y-O.T).dot(X)/int(X.shape[0])#因此，此处求平均，除X的行，即数据量
    W = W + W_C
    
for _ in range(100):#定义一个循环来更新权值
    update()#更新权值
    print(W)#打印当前权值
    print(n)#打印迭代次数
    O = np.sign(np.dot(X,W.T))#计算当前输出
    if(O == Y.T).all():#如果实际输出等于期望输出，模型收敛，循环结束
        print('Finished')
        print('epoch:',n)
        break
        
# 正样本
x1 = [3,4]
y1 = [3,3]
# 负样本
x2 = [1]
y2 = [1]

#得到一组权值将这两类点分开
#计算分界线的斜率和截距
k = -W[1]/W[2]#W0+X1W1+X2W2=0
d = -W[0]/W[2]#X2=-(W1/W2)*X1-W0/W2
print('k=',k)
print('d=',d)

xdata = np.linspace(0,5)

plt.figure()
plt.plot(xdata,xdata*k+d,'r')
plt.plot(x1,y1,'bo')
plt.plot(x2,y2,'yo')
plt.show()