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
"""
练习: 登录判断

已知:
correct_password = "python123"
password: 用户输入的密码
is_locked: 账号是否被锁定
attempts: 本次登录前已连续输错的次数, 假设为非负整数

规则:
1. 账号已锁定, 或 attempts >= 3:
   输出 "账号已锁定".
2. 否则, 密码正确:
   输出 "登录成功".
3. 否则:
   attempts 加 1.
   如果此时 attempts >= 3, 输出 "密码错误, 账号已锁定".
   否则输出 "密码错误, 还剩 X 次机会".

要求:
使用 if / elif / else.
不使用循环.
锁定时不再检查密码.
"""
"""
correct_password = "python123"
password = "abc"
is_locked = False
attempts = 2
if password == correct_password:
    attempts = attempts
    is_locked = False
    print("密码正确")
else:
    attempts+=1
    print("密码错误")
    if attempts >=3:
        attempts = attempts
        is_locked = True
        print("密码输入错误次数过多,账号已锁定")
"""
#先判断账户是否锁定
#更改后
"""
correct_password = "python123"
password = "abc"
is_locked = False
attempts = 2
if is_locked :
    print ("")
elif password == correct_password:
        attempts = attempts
        is_locked = False
        print("密码正确")
else:
    attempts+=1
    print("密码错误")
    if attempts >=3:
        attempts = attempts
        is_locked = True
        print("密码输入错误次数过多,账号已锁定")
"""
#首次全部写对代码


#==for循环==

"""
for i in range(5):   
    print (i)
"""
#range 表示一串规律变化的整数



"""
total = 0
for i in range(1,6):  #取1-6,py规定包含起点不包含终点
    total +=i;
print (total);
#取1+2+3+。。。+5=15
"""
"""
for i in range (1,11,2):
    total +=i
    print (total);
"""
"""
for i in range (1,6):
    if i == 3 :
        continue
    print (i)
"""
