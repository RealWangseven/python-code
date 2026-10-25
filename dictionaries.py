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

"""
练习: 按类别统计支出

每条记录的格式为 "类别,金额".

任务:
1. 遍历 records, 用 split() 拆出类别和金额.
2. 用 int() 将金额转换为整数.
3. 用字典 totals 累加每种类别的支出.
4. 输出完整的支出字典.
5. 查询 travel 的总支出, 不存在时返回 0.
6. 遍历统计结果, 输出总支出 >= 50 的类别和金额.

要求:
累计金额使用 get().
不直接写死统计结果.
不用定义函数.
"""



# records = ["food,25", "books,40", "food,35", "games,60", "books,20"]
# # records: 支出记录列表
# totals = {}  # totals: 各类别的累计支出

# # record: 当前记录
# # category: 支出类别
# # amount: 本笔金额
# # 请在下面编写代码:

# for i in records:
#     category,amount = i.split(",")
#     amount = int(amount)
#     totals[category] = totals.get(category,0) + amount
# print(totals)
# print(totals.get("travel",0))
# for category,amount in totals.items():
#     if amount >= 50:
#         print(category,amount)

"""
练习: 删除下架商品

任务:
1. 从 stock 中删除 milk, 用 removed 接收它原来的库存.
2. 尝试删除 coffee, 不存在时返回 0.
3. 分别输出两次删除返回的值.
4. 输出删除后的完整库存字典.
5. 查询 milk 的库存, 不存在时返回 0.

要求:
使用 pop() 删除, 使用 get() 查询.
"""

# stock = {"apple": 5, "milk": 3, "bread": 8}  # stock: 商品库存

# # removed: 删除时返回的原库存
# # 请在下面编写代码:

# a = stock.pop("milk",0)
# b = stock.pop("coffee",0)
# print(a,b)
# print(stock)
# print(stock.get("milk",0))

"""
练习: 购买商品并计算金额

任务:
1. 商品不存在时, 输出 "Product not found".
2. 购买数量小于等于 0 时, 输出 "Invalid quantity".
3. 库存不足时, 输出 "Insufficient stock".
4. 否则:
   计算总金额.
   扣减该商品库存.
   输出总金额和剩余库存.

要求:
使用嵌套字典.
总金额保留两位小数.
先不用定义函数.
"""

# products = {
#     "apple": {"price": 5, "stock": 10},
#     "milk": {"price": 8, "stock": 3},
#     "bread": {"price": 6, "stock": 5}
# }  # products: 商品资料字典

# product = "milk"  # product: 要购买的商品名
# quantity = 2  # quantity: 购买数量

# # total: 总金额
# # 请在下面编写代码:
# if product not in products:
#     print("Product not found")
# elif quantity <= 0:
#     print("Invalid quantity")
# elif products[product]["stock"] < quantity:
#     print("Insufficient stock")
# else:
#     total = products[product]["price"] * quantity
#     products[product]["stock"] -= quantity

#     print(f"Total: {total:.2f}")
#     print("Stock:",products[product]["stock"])

"""
练习: 计算库存总价值

任务:
1. 遍历 products, 计算每种商品的库存价值:
   单价 * 库存数量.
2. 输出每种商品的名称和库存价值.
3. 累加并输出全部商品的库存总价值.
4. 将库存少于 5 件的商品名添加到 low_stock, 最后输出.

要求:
使用 items() 遍历.
不修改原字典.
金额保留两位小数.
先不用定义函数.
"""

# products = {
#     "apple": {"price": 5, "stock": 10},
#     "milk": {"price": 8, "stock": 3},
#     "bread": {"price": 6, "stock": 5}
# }  # products: 商品资料字典

# total = 0  # total: 全部库存总价值
# low_stock = []  # low_stock: 库存不足 5 件的商品名列表

# # value: 当前商品的库存价值
# # 请在下面编写代码:

# for name, info in products.items():
#     value = info["price"] * info["stock"]
#     print(f"{name}:{value:.2f}")
#     total += value
#     if info["stock"] < 5:
#         low_stock.append(name)
# print(f"{total:.2f}")
# print(low_stock)

"""
练习: 对比赋值与复制

任务:
1. 让 shared = stock.
2. 让 copied = stock.copy().
3. 将 shared 中 apple 的库存改为 10.
4. 将 copied 中 milk 的库存改为 0.
5. 分别输出 stock、shared、copied.

先预测结果, 再运行检查.
本题只使用一层字典.
"""

stock = {"apple": 5, "milk": 3}  # stock: 原库存

# shared: 与原库存共用一个字典
# copied: 复制得到的字典
# 请在下面编写代码:

shared = stock
copied = stock.copy()
shared["apple"] = 10
copied["milk"] = 0
print(stock,shared,copied)
