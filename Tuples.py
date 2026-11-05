"""
练习: 坐标元组

任务:
1. 定义元组 start, 值为 (2, 3).
2. 定义元组 end, 值为 (8, 11).
3. 分别将两个元组拆给四个变量:
   x1, y1, x2, y2.
4. 计算横向变化量 dx 和纵向变化量 dy.
5. 输出 dx、dy.
6. 创建元组 movement, 保存 dx、dy, 并输出.

要求:
用拆包接收坐标, 不逐个通过下标读取.
"""

# start: 起点; end: 终点
# dx: 横向变化量; dy: 纵向变化量
# movement: 位移元组
# 请在下面编写代码:

# import math

# Point = tuple[int, int]

# start: Point = (2, 3)
# end: Point = (8, 11)

# # 用拆包拿到坐标, 不通过下标逐个读取
# x1, y1 = start
# x2, y2 = end

# dx = x2 - x1
# dy = y2 - y1
# movement: Point = (dx, dy)

# print(dx, dy)
# print(movement)

# # 扩展: 两点间的直线距离
# distance = math.hypot(dx, dy)
# print(f"移动距离: {distance}")

"""
练习: 坐标元组

任务:
1. 定义元组 start, 值为 (2, 3).
2. 定义元组 end, 值为 (8, 11).
3. 分别将两个元组拆给四个变量:
   x1, y1, x2, y2.
4. 计算横向变化量 dx 和纵向变化量 dy.
5. 输出 dx、dy.
6. 创建元组 movement, 保存 dx、dy, 并输出.

要求:
用拆包接收坐标, 不逐个通过下标读取.
"""

# start: 起点; end: 终点
# dx: 横向变化量; dy: 纵向变化量
# movement: 位移元组
# 请在下面编写代码:

# start = (2, 3)
# end = (8, 11)
# x1, y1 = start
# x2, y2 = end
# dx = x2 - x1
# dy = y2 - y1
# movement = (dx, dy)

# print(dx, dy)
# print(movement)

"""
练习: 计算订单金额

orders 中每个元组表示:
(商品名, 单价, 购买数量).

任务:
1. 遍历 orders, 将每个元组拆给三个变量.
2. 计算并输出每种商品的小计.
3. 累加订单总金额.
4. 总金额满 50 元减 10 元, 否则不减.
5. 输出实付金额, 保留两位小数.

要求:
使用循环拆包, 不用下标逐个读取.
先不用定义函数.
"""

# orders = [
#     ("apple", 5, 3),
#     ("milk", 8, 2),
#     ("bread", 6, 4)
# ]  # orders: 订单列表, 每项是一个元组

# total = 0  # total: 优惠前总金额

# # name: 商品名
# price: 单价
# quantity: 购买数量
# subtotal: 当前商品的小计
# 提示: for name, price, quantity in orders:
# 请在下面编写代码:

# for name, price, quantity in orders:
#     subtotal = price * quantity
#     print(f"{name} 小计: {subtotal}")
#     total += subtotal

# if total >= 50:
#     total -= 10

# print(f"{total:.2}")

"""
练习: 活动签到核对

任务:
1. 将 registered 和 arrived 分别转换成集合.
2. 找出已报名且到场的人.
3. 找出已报名但没到场的人.
4. 找出没报名却到场的人.
5. 分别输出上述三组人名及人数.

要求:
使用集合运算.
不用循环逐人比较.
集合输出顺序不同不影响正确性.
"""

# registered = ["Alex", "Emma", "Bob", "Daisy", "Alex"]
# # registered: 报名名单
# arrived = ["Emma", "Bob", "Lucy", "Bob"]
# # arrived: 到场名单

# # set(列表): 将列表转换成集合, 自动去重
# # 请在下面编写代码:

# registered = set(registered)
# arrived = set(arrived)

# a = registered & arrived      # 交集: 报名且到场
# b = registered - arrived      # 差集: 报名但没到场
# c = arrived - registered      # 差集: 没报名却到场

# print(f"报名且到场: {a}, {len(a)} 人")
# print(f"报名未到场: {b}, {len(b)} 人")
# print(f"未报名却到场: {c}, {len(c)} 人")

"""
练习: 两门课程的选课统计

已知两门课程的学生名单.

任务:
1. 将两个名单转换成集合.
2. 找出同时选了两门课的人.
3. 找出只选了 Python 的人.
4. 找出只选了 CPP 的人.
5. 合并选课名单, 统计至少选了一门课的总人数.
6. 判断 Alex 是否同时选了两门课, 输出 True 或 False.

要求:
使用集合运算.
不用循环逐人比较.
不用直接写死结果.
"""

# python_students = ["Alex", "Emma", "Bob", "Daisy"]
# # python_students: Python 课程名单
# cpp_students = ["Alex", "Bob", "Lucy", "Tom"]
# # cpp_students: CPP 课程名单

# # set(): 转成集合
# # &: 交集, 两边都有
# # -: 差集, 左边有而右边没有
# # |: 并集, 合并并去重
# # in: 判断成员是否存在
# # 请在下面编写代码:

# python_students = set(python_students)
# cpp_students = set(cpp_students)

# a = python_students & cpp_students      # 同时选两门
# b = python_students - cpp_students      # 只选 Python
# c = cpp_students - python_students      # 只选 CPP
# j = python_students | cpp_students      # 至少选了一门

# x = "Alex" in a                         # Alex 是否同时选了两门

# print(f"同时选两门: {a}, {len(a)} 人")
# print(f"只选 Python: {b}, {len(b)} 人")
# print(f"只选 CPP: {c}, {len(c)} 人")
# print(f"至少选一门总人数: {len(j)} 人")
# print(x)
