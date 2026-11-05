"""
练习: 安全除法

任务:
1. 输入两个整数 a 和 b.
2. 输出 a / b 的结果, 保留两位小数.
3. 输入不能转成整数时, 输出 "Invalid integer".
4. 除数为 0 时, 输出 "Cannot divide by zero".

要求:
使用 try / except.
两个异常分别处理.
计算成功时才输出结果.
暂时不使用循环.

提示:
ValueError: 整数转换失败.
ZeroDivisionError: 除以零.
"""

# 请在下面编写代码:

try:
    a = int(input("请输入 a: "))   # 转换失败 → ValueError
    b = int(input("请输入 b: "))
    result = a / b                 # b 为 0 → ZeroDivisionError
except ValueError:
    print("Invalid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    # try 块全部成功才执行 else
    print(f"{result:.2f}")
