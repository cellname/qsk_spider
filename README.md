# python基础巩固练习

题目1：有四个数字：1,2,3,4，能组成多少个互不相同且无重复数字的三位数，各是多少
程序分析：遍历全部可能，把有重复的剔除掉
itertools --- 为高效循环而创建迭代器的函数 连接：https://docs.python.org/zh-cn/3/library/itertools.html

题目2：企业发放的奖金根据利润提成：
利润<=10w ,奖金可提10%
10w <利润<20w,低于10w部分可提10%，高于10w部分提7.5%  
20w <利润<40w,高于20w部分提5%                     
40w <利润<60w,高于40w部分提3%
60w <利润<100w,高于60w部分提1.5%
利润>100w ,高于100万部分提1%

题目3:将一个列表的数据复制到另外一个列表中
程序分析：可以使用[:],也可以使用copy模块

题目4：输出9*9乘法口诀表

题目5：暂停一秒输出，并格式化显示当前时间
