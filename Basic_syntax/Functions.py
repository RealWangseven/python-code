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



# scores = [72, 85, 59, 90, 66]  # scores: 成绩列表

# # average: 平均分函数
# # 请在下面编写代码:
# total = sum(scores)
# def average(scores):
#     return total / len(scores)
#     result = average(scores)
# print(f"{result:.2f}")

"""
练习: 用同一个函数计算两组平均分

任务:
1. 保留你写好的 average(scores) 函数.
2. 分别把下面两个列表传给函数.
3. 将两个返回值保存到 avg_a 和 avg_b.
4. 输出两组平均分, 保留两位小数.
5. 用条件判断输出哪组平均分更高, 相等则输出 "两组相同".

要求:
只定义一次 average 函数.
不要在函数里固定使用某一组成绩.
"""




# group_a = [80, 90, 70]  # group_a: A 组成绩
# group_b = [60, 75, 85, 100]  # group_b: B 组成绩

# # avg_a: A 组平均分
# # avg_b: B 组平均分
# # 请在下面编写代码:
# def average(scores):
#     total = sum(scores)
#     return total / len(scores)
# avg_a = average(group_a)
# avg_b = average(group_b)

# print(f"{avg_a:.2f},{avg_b:.2f}")
# if avg_a > avg_b:
#     print("a is bigger")
# elif avg_a < avg_b:
#     print("b is bigger")
# else:
#     print("same")

"""
练习: 折后价格函数

任务:
1. 定义函数 discounted_price(price, rate).
2. 接收原价和折扣比例, 返回折后价格.
3. 分别调用函数, 计算:
   原价 200 元, 打八折.
   原价 150 元, 打九折.
4. 在函数外输出两个结果, 保留两位小数.

要求:
函数内不写 print().
只定义一次函数, 调用两次.
折扣比例用小数表示, 例如八折为 0.8.
"""

# discounted_price: 折后价格
# price: 原价
# rate: 折扣比例
# 请在下面编写代码:

# def discounted_price(price, rate):
#     return price * rate
# a =discounted_price(200,0.8)
# b = discounted_price(150,0.9)
# print(f"{a:.2f},{b:.2f}")

"""
练习: 满减与会员折扣

定义函数 final_price(price, is_member), 返回实付金额.

计价规则:
1. 原价满 300 元, 先减 50 元; 不满则不减.
2. 如果是会员, 在满减后的金额上再打八折.
3. 非会员只享受满减.

任务:
调用同一个函数计算:
1. 原价 400 元, 是会员.
2. 原价 200 元, 是会员.
3. 原价 400 元, 不是会员.

在函数外输出三个结果, 均保留两位小数.

要求:
函数内使用 if 判断.
函数内不写 print().
不要直接写出计算结果.
"""

# final_price: 实付金额函数
# price: 原价
# is_member: 是否为会员
# 请在下面编写代码:

# def final_price(price, is_member):
#     if price >= 300:
#         price -= 50
#     if is_member == True:
#         price *= 0.8
#     return price;

# a = final_price(400, True)
# b = final_price(200, True)
# c = final_price(400, False);

# print(f"{a:.2f},{b:.2f},{c:.2f}");

"""
练习: 运费计算函数

定义函数 shipping_fee(amount, is_remote=False).

规则:
1. 订单金额满 99 元, 基础运费为 0 元.
2. 不满 99 元, 基础运费为 10 元.
3. 偏远地区在基础运费上加收 15 元.

任务:
计算并输出以下订单的运费:
1. 金额 120 元, 使用默认地区.
2. 金额 60 元, 使用默认地区.
3. 金额 120 元, 属于偏远地区.

要求:
函数内返回运费, 不写 print().
前两次调用省略第二个参数.
"""

# shipping_fee: 运费函数
# amount: 订单金额
# is_remote: 是否为偏远地区, 默认 False
# fee: 运费
# 请在下面编写代码:

# def shipping_fee(amount, is_remote=False):
#     if amount >= 99:
#         fee = 0
#     else:
#         fee = 10
#     if is_remote == True:
#         fee += 15
#     return fee;

# a = shipping_fee(120)
# b = shipping_fee(60)
# c = shipping_fee(120, True);

# print(f"{a:.2f},{b:.2f},{c:.2f}")

"""
练习: 关键字参数

保留你写好的 shipping_fee 函数.

任务:
1. 金额 60 元, 偏远地区:
   用关键字参数调用, 先写 is_remote, 再写 amount.
2. 金额 120 元, 非偏远地区:
   只传 amount, 使用默认地区.
3. 分别接收返回值, 并输出运费, 保留两位小数.

要求:
不修改函数定义.
"""

# 请在下面编写两次调用和输出:

# def shipping_fee(amount, is_remote=False):
#     if amount >= 99:
#         fee = 0
#     else:
#         fee = 10
#     if is_remote == True:
#         fee += 15
#     return fee;

# a = shipping_fee(is_remote=True,amount=60)
# b = shipping_fee(amount=120)

# print(f"{a:.2f},{b:.2f}")

"""
练习: 成绩统计函数

定义函数 analyze(scores), 接收非空成绩列表.

任务:
1. 在函数内计算总分和平均分.
2. 按顺序返回总分、平均分.
3. 在函数外用两个变量接收.
4. 输出总分和平均分, 平均分保留两位小数.

要求:
可以使用 sum() 和 len().
函数内不写 print().
"""

# scores = [72, 85, 59, 90, 66]  # scores: 成绩列表

# # analyze: 分析
# # total: 总分
# # average: 平均分
# # 请在下面编写代码:

# def analyze(data):
#     total = sum(data)
#     average = total / len(data)
#     return total,average
# total,average = analyze(scores)
# print(f"{total},{average:.2f}")

"""
练习: 及格成绩统计函数

定义函数 passing_stats(data), 接收非空成绩列表.

任务:
1. 用循环统计及格人数, 60 分及以上为及格.
2. 累加所有及格成绩.
3. 计算及格者的平均分.
4. 按顺序返回及格人数、及格者平均分.
5. 在函数外接收并输出结果, 平均分保留两位小数.

特殊情况:
如果没有人及格, 返回 0, 0.
注意不能除以 0.

检查:
两组成绩都要调用同一个函数.
函数内不写 print().
"""

# group_a = [80, 45, 72, 58, 90]  # group_a: A 组成绩
# group_b = [30, 42, 59]  # group_b: B 组成绩

# passing_stats: 及格成绩统计函数
# data: 本次传入的成绩列表
# count: 及格人数
# total: 及格成绩总分
# average: 及格者平均分
# 请在下面编写代码:

# def passing_stats(data):
#     grade = 0
#     count = 0 
#     total = 0
#     average = 0 
#     for grade in data:
#         if grade >= 60:
#             total += grade
#             count += 1
#     if count == 0:
#         return 0,0
#     average = total / count
#     return count,average;

# counta,avg_a = passing_stats(group_a)
# countb,avg_b = passing_stats(group_b);

# print(f"{counta},{avg_a:.2f}")  
# print(f"{countb},{avg_b:.2f}")   
    
"""
练习: 商品优惠统计函数

定义函数 sale_stats(data, threshold=100).

规则:
1. 只有价格 >= threshold 的商品参与优惠.
2. 参与优惠的商品统一打八折.

任务:
1. 用循环统计参与优惠的商品数量.
2. 累加这些商品的原价, 再计算折后总价.
3. 按顺序返回商品数量、折后总价.
4. 没有符合条件的商品时, 返回 0, 0.

分别调用:
1. 使用默认门槛 100.
2. 指定门槛为 200.

在函数外输出数量和折后总价, 金额保留两位小数.

要求:
函数内不写 print().
"""



# prices = [35, 120, 88, 200, 150]  # prices: 商品价格列表

# # sale_stats: 优惠统计函数
# # data: 本次传入的价格列表
# # threshold: 参与优惠的价格门槛, 默认 100
# # count: 符合条件的商品数量
# # total: 符合条件商品的原价总和
# # 请在下面编写代码:
# def sale_stats(data, threshold=100):
#     total = 0
#     count = 0
#     for price in data:
#         if price >= threshold:
#             count += 1
#             total += price

#     total *=0.8

#     return count,total
# a1,a2 = sale_stats(prices)
# b1,b2 = sale_stats(prices,threshold=200)
# print(f"{a1:.2f},{a2}")
# print(f"{b1:.2f},{b2}")
        
    
"""
2026/10/24
"""

"""
练习: 同时返回和与积

1. 定义函数 calculate(a, b).
2. 按顺序返回两个数的和、两个数的乘积.
3. 调用函数, 传入 6 和 4.
4. 用两个变量分别接收结果, 并输出.

要求:
函数内不写 print().
"""

# calculate: 计算
# total: 两数之和
# product: 两数之积
# 请在下面编写代码:

# def calculate(a,b):
#     total = a + b
#     product = a * b
#     return total,product
# i,j = calculate(6,4)
# print(i,j)

"""
练习: 两组成绩比较

编写两个函数:

1. analyze(data)
   接收非空成绩列表.
   返回总分、平均分.

2. compare(data_a, data_b)
   在内部调用 analyze(), 分别获取两组的总分和平均分.
   比较平均分, 返回以下三个结果:
   - 较高平均分对应的组名: "A组"、"B组" 或 "相同".
   - A组平均分.
   - B组平均分.

在函数外:
调用 compare(), 用三个变量接收结果并输出.
平均分保留两位小数.

要求:
compare() 内不能重复计算总分和平均分, 必须调用 analyze().
两个函数内部都不写 print().
"""



# group_a = [80, 95, 65]  # group_a: A组成绩
# group_b = [72, 88, 91, 85]  # group_b: B组成绩

# # analyze: 分析
# # compare: 比较
# # data_a、data_b: 传入的两组成绩
# # winner: 比较结果
# # 请在下面编写代码:

# def analyze(data):
#     total = 0
#     for grade in data:
#         total += grade
#     average = total / len(data)
#     return total,average;

# def compare(data_a,data_b):
#     total_a,avg_a = analyze(data_a)
#     total_b,avg_b = analyze(data_b)
#     if avg_a > avg_b:
#         return "A组",avg_a,avg_b
#     if avg_a < avg_b:
#         return "B组",avg_a,avg_b
#     else:
#         return "相同",avg_a,avg_b
# winer,avg_a,avg_b = compare(group_a,group_b)
# print(f"{winer},{avg_a:.2f},{avg_b:.2f}")

"""
练习: 筛选及格成绩

定义函数 select_scores(data, threshold=60).

任务:
1. 在函数内创建空列表 result.
2. 遍历 data, 将 >= threshold 的成绩添加到 result.
3. 返回 result.

在函数外:
1. 使用默认门槛调用, 输出筛选结果.
2. 指定门槛为 80 再调用, 输出筛选结果.
3. 计算第二次筛选结果的平均分, 保留两位小数.
   如果结果为空, 输出 "没有符合条件的成绩".

要求:
原列表保持不变.
函数内不写 print().
"""




# scores = [45, 80, 62, 91, 58, 76]  # scores: 原始成绩

# select_scores: 筛选成绩函数
# data: 传入的成绩列表
# threshold: 筛选门槛
# result: 筛选结果, 用 [] 创建空列表
# append(): 向列表末尾添加元素
# len(result) == 0: 判断列表是否为空
# 请在下面编写代码:

# def select_scores(data, threshold=60):
#     result = []
#     for grade in data:
#         if grade >= threshold:
#             result.append(grade)
#     return result
# passedA = select_scores(scores)
# passedB = select_scores(scores,threshold=80)

# average = round(sum(select_scores(scores,threshold=80)) / len(select_scores(scores,threshold=80)),2)
# if len(passedB) == 0:
#     print("没有符合条件的成绩")
# else:
#     print(f"{average}")

"""
练习: 筛选偶数并倒序

定义函数 select_even(data).

任务:
1. 在函数内创建空列表 result.
2. 遍历 data, 将偶数添加到 result.
3. 返回 result.

在函数外:
1. 调用函数, 用一个变量接收整个结果列表.
2. 输出筛选后的列表.
3. 用切片将筛选结果倒序, 再输出.
4. 输出原列表, 确认它没有改变.

要求:
函数内不写 print().
不直接写死筛选结果.
"""



# numbers = [13, 8, 21, 6, 17, 10, 4]  # numbers: 原始数字列表

# select_even: 筛选偶数
# data: 传入的列表
# result: 筛选结果列表
# selected: 函数外接收的结果列表
# 请在下面编写代码:

# def select_even(data):
#     result = []
#     for i in data:
#         if i % 2 == 0:
#             result.append(i)
#     return result;
# j = select_even(numbers)
# print(j)
# j = j[::-1]
# print(j)
# print(numbers)

