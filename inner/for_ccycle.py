"""
    for 循环
        拿
            for item in 容器：
                循环体
"""

# massage = "我爱python编程"
# for item in massage:
#     print(item)

"""
exercise1
在终端中输入任意整数，计算累加和.
"1234" -> "1" -> 累加 1
效果：
请输入一个整数:12345
累加和是 15
"""
add_integer=0
integer = input("请输入任意的整数：")
for item in integer:
    add_integer+=int(item)
print(add_integer)


