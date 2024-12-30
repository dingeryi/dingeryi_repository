"""
    循环
        while True:              延长程序生命
            循环体
            if 条件：
                break
"""
while True:
    if input("请输入性别：") == "男":
        print("您好先生")
    else:
        print("您好女士")
    print("欢迎光临！")
    if input("请输入q键退出:") == "q":
        break     #结束循环






