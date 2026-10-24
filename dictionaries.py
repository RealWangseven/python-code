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

stock = {"apple": 5, "milk": 3, "bread": 8}  # stock: 商品库存
product = "milk"  # product: 要购买的商品名
quantity = 2  # quantity: 购买数量

# 提示: product not in stock 表示商品不存在.
# 请在下面编写代码: