
'''
题目1：有四个数字：1,2,3,4，能组成多少个互不相同且无重复数字的三位数，各是多少
程序分析：遍历全部可能，把有重复的剔除掉
itertools --- 为高效循环而创建迭代器的函数 连接：https://docs.python.org/zh-cn/3/library/itertools.html
'''
import itertools
sum1 = 0
a = [1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum1 += 1
print(sum1)

"""
题目2：企业发放的奖金根据利润提成：
利润<=10w ,奖金可提10%
10w <利润<20w,低于10w部分可提10%，高于10w部分提7.5%  
20w <利润<40w,高于20w部分提5%                     
40w <利润<60w,高于40w部分提3%
60w <利润<100w,高于60w部分提1.5%
利润>100w ,高于100万部分提1%

程序分析：分区间计算即可
"""

profit = int(input('show me the money:'))
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)

'''
题目3:将一个列表的数据复制到另外一个列表中
程序分析：可以使用[:],也可以使用copy模块
'''
import copy
a = [1,2,3,4,["a","b"]]
# 赋值
b = a
# 浅拷贝
c = a[:]
# 浅拷贝
d = copy.copy(a)
# 深拷贝
e = copy.deepcopy(a)

a.append(5)
a[4].append('e')

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print('e=',e)

'''
题目4：输出9*9乘法口诀表
程序分析：分行与分列考虑，共9行9列，i控制行，j控制列
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j),end=" ")
    print()

'''
题目5：暂停一秒输出，并格式化显示当前时间
'''
import time
for i in range(10):
    print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime((time.time()))))
    time.sleep(1)