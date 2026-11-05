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

# try:
#     a = int(input("请输入 a: "))   # 转换失败 → ValueError
#     b = int(input("请输入 b: "))
#     result = a / b                 # b 为 0 → ZeroDivisionError
# except ValueError:
#     print("Invalid integer")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     # try 块全部成功才执行 else
#     print(f"{result:.2f}")

"""
练习: 安全计算平均分

任务:
1. 用 input() 输入一组成绩, 用英文逗号分隔.
2. 拆分后, 将每项转换为整数并放入列表.
3. 计算平均分, 输出时保留两位小数.
4. 如果输入为空或只有空格, 输出 "No scores".
5. 如果有内容无法转换成整数, 输出 "Invalid score".

要求:
使用 try / except ValueError.
先检查整段输入是否为空, 再拆分和计算.
暂时不检查成绩是否在 0-100 之间.
不用定义函数.

检查用例:
80,90,70 -> 80.00
80,abc,90 -> Invalid score
只输入空格 -> No scores
"""

# text: 用户输入的文字
# scores: 转换后的整数列表
# average: 平均分
# ValueError: int() 无法转换输入时产生的异常
# 请在下面编写代码:

# text = input("请输入成绩(用英文逗号分隔): ")

# if not text.strip():
#     # 空串或只有空格
#     print("No scores")
# else:
#     try:
#         # 按逗号拆分, 每一项转成整数
#         scores = [int(part) for part in text.split(",")]
#         average = sum(scores) / len(scores)
#     except ValueError:
#         print("Invalid score")
#     else:
#         print(f"{average:.2f}")