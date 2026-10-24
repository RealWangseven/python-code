"""
练习: 编写平均分函数

任务:
1. 定义函数 average(scores), 接收一个非空成绩列表.
2. 在函数内计算平均分, 并用 return 返回.
3. 调用函数, 接收返回值.
4. 在函数外输出平均分, 保留两位小数.

要求:
可以使用 sum() 和 len().
函数内不写 print().
"""



scores = [72, 85, 59, 90, 66]  # scores: 成绩列表

# average: 平均分函数
# 请在下面编写代码:
total = sum(scores)
def average(scores):
    return total / len(scores)
    result = average(scores)
print(f"{result:.2f}")