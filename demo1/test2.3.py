#实现与门，与非门，或门 的感知机
#参考《深度学习入门-基于Python的理论与实现》2.3节
import numpy as np
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

print(AND(1,0))

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

print(NAND(1,1))

def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

print(OR(0,1))


#多层感知机
#异或门:有且只有一个输入为真才输出为真
#异或门的实现：与非门和或门的输入，而与非门和或门的输出则是与门的输入。
def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y
print('-----多层感知机实现异或门----')
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))


