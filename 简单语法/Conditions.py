#小练习

'''
score = 85;
if score >= 85:
    print("及格");
if score < 85:
    print("不及格");
'''
"""
ages = {"李相赫":29,"360":25,"bin":23,"the shy":26}
name = "李相赫","369","bin","the shy"
for name in ages:
    if ages[name] < 25:
     print (f"{name}是冠军🏆！！！")
"""
"""
练习: 停车费计算

变量:
hours: 停车时长, 假设为整数, 单位为小时.
is_member: 是否为会员, True 为是, False 为否.

收费规则:
1. 有效时长为 1-24 小时, 超出范围只输出 "时长无效".
2. 分段累计收费:
   前 2 小时, 每小时 5 元;
   第 3-6 小时, 每小时 4 元;
   超过 6 小时的部分, 每小时 3 元.
3. 会员享受总费用八折优惠.

要求:
使用变量和 if / elif / else, 不使用循环.
有效时输出 "停车费: XX.XX 元", 保留两位小数.
无效时不计算或输出停车费.

检查用例:
1 小时, 非会员 -> 停车费: 5.00 元
5 小时, 会员 -> 停车费: 17.60 元
8 小时, 非会员 -> 停车费: 32.00 元
0 小时, 会员 -> 时长无效
"""
"""
hours = 5
is_member = True
if is_member :
    print("这是会员,停车费17.6元")
else :
    print("这不是会员,停车费18元")
"""
#确实写得不好。。。


"""
hours = 5
is_member = True
al = hours * 5
be = 2 * 5 + (hours - 2) * 4
ch = 2 * 5 + 4 * 4 + (hours - 6) * 3

alm = al * 0.8
bem = be * 0.8
chm = ch * 0.8

fee = (al,alm,be,bem,ch,chm);

if is_member:
    if hours<=2:
        fee=alm
    elif hours<=5:
        fee=bem
    else:
        fee=chm;
    print(f"您是会员,您的停车费用是{fee:.2f}元")
else:
    if hours<=2:
        fee=al
    elif hours<=5:
        fee=be
    else:
        fee=ch;
    print(f"您不是会员,您的停车费用是{fee:.2f}元")
"""
#终于！
