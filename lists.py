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

