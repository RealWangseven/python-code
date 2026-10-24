"""
练习: 列表基础

知识点:
list: 列表, 用于保存多个值, 可以类比 C++ 的 vector.
列表使用方括号 [], 元素之间用逗号分隔.
下标从 0 开始, scores[0] 表示第一个元素.

示例:
scores = [85, 92, 78]
print(scores[0])  # 输出 85
scores[1] = 95    # 将第二个成绩改成 95

任务:
1. 定义列表 scores, 保存成绩 85, 92, 78, 60.
2. 输出第一个成绩.
3. 将第二个成绩改成 95.
4. 输出最后一个成绩.
5. 输出修改后的完整列表.

要求:
先直接在 [] 中写入四个成绩.
本题不用循环.
"""

# 请在下面编写代码:
# scores = [85,92,78,60];
# print(scores[0]);
# scores[1] = 95;
# print(scores[3]);   # -1 表示最后一个元素,以此类推
# print(scores);
"""
练习: 成绩列表处理

已知成绩列表 scores, 完成以下任务:

1. 输出最后一个成绩, 使用负数下标.
2. 将第二个成绩增加 5 分.
3. 用循环计算总分, 不使用 sum().
4. 计算平均分.
5. 统计及格人数, 成绩 >= 60 为及格.

最后输出:
修改后的完整列表.
总分.
平均分, 保留两位小数.
及格人数.

提示:
for score in scores:
    可以依次取出列表里的每个成绩.
len(scores) 可以获取列表的元素个数.
"""

# scores = [85, 57, 92, 43, 76]  # scores: 成绩列表
# total = 0  # total: 总分
# passed = 0  # passed: 及格人数

# # 请在下面编写代码:
# print(scores[-1]);
# scores[1] += 5;
# total = sum(scores);
# average = total / len(scores);
# for score in scores:
#     if score >=60:
#         passed += 1;
# print(f"{passed}人及格");
"""
练习: 统计商品价格

已知价格列表 prices, 完成以下任务:

1. 用循环统计价格 >= 100 元的商品数量.
2. 用循环计算这些商品的总价.
3. 如果总价 >= 300 元, 减免 50 元; 否则不减免.
4. 输出符合条件的商品数量、优惠前总价、实付金额.
   金额保留两位小数.

要求:
只统计价格 >= 100 元的商品.
使用 for 和 if, 不需要 input().
"""

# prices = [35, 120, 88, 200, 150]  # prices: 商品价格列表
# count = 0  # count: 符合条件的商品数量
# total = 0  # total: 符合条件的商品总价
# afttotal = 0
# # 请在下面编写代码:
# for a in prices:
#     if a >= 100:
#      count += 1
#      total += a
# print(f"{count}....")
# if total >= 300:
#     afttotal = total - 50
# else:
#     total = total;
# print(f"{count},{total},{afttotal}")
"""
有点绕
"""
"""
练习: 统计不及格成绩

任务:
1. 遍历成绩列表, 找出低于 60 分的成绩.
2. 统计不及格人数.
3. 计算这些人距离 60 分一共差多少分.
4. 如果没有不及格的人, 输出 "全部及格".
   否则输出不及格人数和总共差的分数.

例如:
45 分距离及格差 15 分.
58 分距离及格差 2 分.

要求:
使用 for 和 if.
不要直接写出统计结果.
"""

# scores = [80, 45, 72, 58, 90, 30]  # scores: 成绩列表
# count = 0  # count: 不及格人数
# gap = 0  # gap: 距离及格总共差的分数

# # 请在下面编写代码:
# for f in scores:
#     if f < 60:
#         count += 1;
#         gap += 60 - f;
#     if count == 0:
#         print("全部及格");
#     else:
#         print(f"总共不及格{count}人,总共差{gap}分");

"""
练习: 去掉一个最高分和一个最低分

任务:
1. 用循环找出最高分和最低分, 不使用 max() 和 min().
2. 计算去掉一个最高分和一个最低分后的平均分.
3. 输出最高分、最低分和处理后的平均分.
4. 平均分保留两位小数.

提示:
先把第一个成绩当作当前最高分和最低分.
遍历时, 遇到更高或更低的成绩就更新对应变量.
总分可以使用 sum(), 成绩个数使用 len().
"""

# scores = [82, 95, 67, 88, 73, 90]  # scores: 成绩列表
# highest = scores[0]  # highest: 当前最高分
# lowest = scores[0]  # lowest: 当前最低分

# # 请在下面编写代码:

# for i in scores:
#     if i > highest:
#         highest = i;
#         print(highest)
#     if i < lowest:
#         lowest = i;
#         print(lowest)
# total = sum(scores)
# a = (total - highest - lowest) / 4
# print(f"{a:.2f}");

"""
练习: 修改成绩列表

初始成绩为 [72, 85, 59].

任务:
1. 在末尾添加成绩 90.
2. 删除下标为 1 的成绩.
3. 将最后一个成绩增加 5 分.
4. 输出最终列表和平均分, 平均分保留两位小数.
"""

# from re import A


# scores = [72, 85, 59]  # scores: 成绩列表

# # 请在下面编写代码:

# scores.append(90)
# scores.pop(1)
# scores[-1] += 5
# total = sum(scores)
# a = total / len(scores)
# print (f"{a:.2f}")
"""
练习: 列表切片

已知成绩列表 scores.

任务:
1. 用切片取出前三个成绩, 存入 first_three.
2. 用切片取出最后两个成绩, 存入 last_two.
3. 分别输出这两个新列表.
4. 计算前三个成绩的平均分, 保留两位小数.

提示:
负数下标也能用于切片.
"""

# scores = [72, 85, 59, 90, 66]  # scores: 成绩列表
# first_three = 0
# last_two = 0

# # first_three: 前三个成绩
# # last_two: 最后两个成绩
# # 请在下面编写代码:

# first_three = scores[:3]
# last_two = scores [3:]
# print(first_three,last_two)
# total = sum(first_three)
# a = total / len(first_three);
# print(f"{a:.2f}")

"""
练习: 带步长的切片

任务:
1. 取出下标为 0, 2, 4, 6 的元素, 存入 selected.
2. 将整个列表倒序取出, 存入 reversed_numbers.
3. 分别输出两个结果.
4. 输出原列表, 观察它是否发生变化.

要求:
使用切片, 不使用循环.
"""

numbers = [12, 25, 38, 41, 56, 63, 70]  # numbers: 数字列表

# selected: 选出的元素
# reversed_numbers: 倒序得到的列表
# 请在下面编写代码:

