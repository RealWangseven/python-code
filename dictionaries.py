"""
练习: 商品购买判断

任务:
1. 如果商品不存在, 输出 "Product not found".
2. 如果购买数量小于等于 0, 输出 "Invalid quantity".
3. 如果库存不足, 输出 "Insufficient stock".
4. 否则扣减库存, 输出 "Purchase successful".
5. 最后输出完整库存字典.

要求:
使用 if / elif / else.
商品不存在时, 不能继续读取它的库存.
先不用定义函数.
"""

# stock = {"apple": 5, "milk": 3, "bread": 8}  # stock: 商品库存
# product = "milk"  # product: 要购买的商品名
# quantity = 2  # quantity: 购买数量

# # 提示: product not in stock 表示商品不存在.
# # 请在下面编写代码:

# if product not in stock:
#     print("Product not found")
# elif quantity <= 0:
#     print("Invalid quantity")
# elif stock[product] < quantity:
#     print("Insufficient stock")
# else:
#     stock[product] -= quantity
#     print("Purchase successful") 
# print(stock);

"""
练习: 库存补货清单

任务:
1. 遍历 stock, 找出库存少于 5 的商品.
2. 创建字典 restock, 保存这些商品需要补货的数量.
3. 每种商品补到 5 件即可.
4. 输出补货字典, 以及总共需要补货多少件.

例如:
库存 2 件, 需要补 3 件.
库存 5 件, 不需要补货.

要求:
使用 items() 遍历.
原库存字典保持不变.
先不用定义函数.
"""



# stock = {"apple": 2, "milk": 5, "bread": 1, "coffee": 0}
# # stock: 当前库存
# restock = {}  # restock: 补货字典, {} 表示空字典
# total = 0  # total: 总补货数量

# # product: 商品名
# # quantity: 当前库存
# # 提示: restock[product] = 数量, 可以新增一组键和值.
# # 请在下面编写代码:

# for product,quantity in stock.items():
#     if quantity < 5:
#         restock[product] = 5 - quantity
#         needed = restock[product]
#         total += needed
# print(restock,total)

"""
练习: 统计商品出现次数

任务:
1. 遍历 products.
2. 用字典 counts 统计每种商品出现了几次.
3. 输出完整的统计字典.
4. 用 get() 查询 "coffee" 的次数, 不存在时按 0 次处理.

要求:
使用循环和 get().
不直接写死统计结果.
"""

# products = ["apple", "milk", "apple", "bread", "milk", "apple"]
# # products: 商品名称列表
# counts = {}  # counts: 各商品出现次数

# # product: 当前商品名
# # 请在下面编写代码:

# for times in products:
#     counts [times] = counts.get(times,0) + 1
# print(counts)
# print(counts.get("coffee",0))

"""
练习 : 统计投票

任务:
1. 遍历 votes, 使用 get() 统计每个人的票数.
2. 输出完整票数字典.
3. 查询 Emma 的票数, 没有记录时返回 0.
4. 查询 Lucy 的票数, 没有记录时返回 0.
5. 遍历票数字典, 输出获得至少 2 票的人名和票数.

要求:
不直接写死统计结果.
统计使用 get(), 遍历字典使用 items().
查询不存在的人时, 不往字典里新增记录.
"""



# votes = ["Alex", "Emma", "Alex", "Bob", "Emma", "Alex", "Daisy"]
# # votes: 投票记录, 每个名字代表获得一票
# counts = {}  # counts: 各人的票数

# # name: 当前人名
# # count: 当前人的票数
# # 请在下面编写代码:

# for ticket in votes:
#     counts[ticket] = counts.get(ticket,0)+1
# print(counts)
# print(counts.get("Emma",0))
# print(counts.get("Lucy",0))

# for name,count in counts.items():
#     if count >= 2:
#         print(name,count)

