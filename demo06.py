"""
    while 循环计数
"""  # 三要素

# 计时器
# count = 0           #开始
# while count<=5:     #结束
#     print(count)
#     count +=1       #间隔

"""
exercise1
在终端中显示0 1 2 3
在终端中显示2 3 4 5 6
在终端中显示1 3 5 7
在终端中显示8 7 6 5 4
在终端中显示-1 -2 -3 -4 -5
"""

# begin=0
# while begin<4:
#     print(begin)
#     begin+=1
# begin = 0
# while begin < 7:
#     begin += 2
#     print(begin)

# exercise2
"""
一张纸的厚度是0.01毫米
请计算，对折多少次超过珠穆朗玛峰(8844.43米)
思路:
数据：厚度、高度、次数
算法：厚度*=2
次数+=1"""

thickness = 1e-5
count = 0
while thickness < 8844.43:
    count += 1
    thickness *= 2
print("总共需要对折："+str(count))
















