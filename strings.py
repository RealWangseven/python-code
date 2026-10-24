"""
练习: 把文字成绩转换成整数列表

任务:
1. 用 split() 按逗号拆分 text, 保存到 parts.
2. 创建空列表 scores.
3. 遍历 parts, 把每项用 int() 转成整数,
   再添加到 scores.
4. 输出 scores.
5. 计算平均分, 输出时保留两位小数.

要求:
本题不用定义函数.
可以使用 sum() 和 len().
"""

# text = "72,85,59,90,66"  # text: 原始成绩文字

# # parts: 拆分后的字符串列表
# # scores: 转换后的整数列表
# # 请在下面编写代码:

# parts = text.split(",")
# scores = []

# for i in parts:
#     scores.append(int(i));

# print(scores)

# average = sum(scores) / len(scores)
# print(f"{average:.2f}")

"""
练习: 清理姓名列表

任务:
1. 按逗号拆分 text.
2. 用 strip() 去掉每个姓名两端的空格.
3. 清理后若为 "", 就跳过.
4. 将非空姓名添加到 names.
5. 输出姓名列表和人数.

要求:
不用定义函数.
保留姓名中间的空格.
"""

text = "  Alex , Emma, , Mary Jane ,   "  # text: 原始姓名文字
names = []  # names: 清理后的姓名列表

# parts: 拆分结果
# name: 当前姓名
# clean: 清理后的姓名
# 请在下面编写代码:

