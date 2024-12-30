"""
随机数
    程序产生1个,1到100之间的随机数。
让玩家重复猜测,直到猜对为止。
每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
"""

# 准备随机数工具
import random

# 产生一个随机数
random_number = random.randint(1, 100)
count = 0
while True:

    num = int(input("请输入一个数："))
# while True:
    count += 1
    if random_number > num:
        print("猜小了")
    elif random_number < num:
        print("猜大了")
    else:
        print("恭喜答对了，总共猜了" + str(count) + "次")

