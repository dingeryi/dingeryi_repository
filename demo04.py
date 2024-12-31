"""
    选择语句
            根据条件执行
            if 条件：
                    满足条件执行的代码
            else：
                    不满足条件执行的代码

            代码
"""

# if input("请输入性别：")=="男":
#     print("您好先生")
# else:
#     print("您好女士")
# print("欢迎光临！")
#


sex=input("请输入性别：")
if sex=="男":
    print("您好先生")
elif sex=="女":      #否则如果
    print("您好女士")
else:
    print("欢迎光临！")

# 调试
# 定义:让程序中断，逐语句执行，
#       审查执行过程与变量取值

#步骤：加断点、开始调试、逐语句执行F8
#重点：
#       按下F8之前-目标-应该是什么
#       按下F8之后-现状-又是什么

#exercise1
integer = int(input("请输入一个整数："))
if integer>0:
    print("你输入的是正数。")
elif integer<0:
    print("你输入的是负数。")
else:
    print("你输入的是0，既不是正数也不是负数")

#exercise2
height1=float(input("请输入第一个同学的身高："))
height2=float(input("请输入第二个同学的身高："))
height3=float(input("请输入第三个同学的身高："))
height4=float(input("请输入第四个同学的身高："))

max=height1

if height1<height2:
    max=height2
if height2<height3:
    max=height3
if height3<height4:
    max=height4


print("身高最高是:"+str(max))


#exercise3
mouth= int(input("请输入一个月份,我来告诉你这个月有几天："))
if 1<=mouth<=12:
    if mouth==2:
        print(str(mouth)+"有29天")
    elif mouth==4 or mouth==6 or mouth==9 or mouth==11:        #不能写成mouth== 4 or 6 or 9 or 11
        print("30天")
    else:
        print("31tian")
else:
    print("有误")




