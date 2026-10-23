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
# for i in range (1,100):
#     if i % 2 ==0 :
#         continue
#     print (i);

# a = 1
# while a <=10:
#     a += a
#     print(a)

"""
综合练习: 猜数字游戏

目标:
程序预设一个 1-100 的整数, 玩家最多猜 5 次.

规则:
1. 每轮用 input() 输入猜测值, 用 int() 转成整数.
   假设玩家只输入整数, 暂不处理非整数输入.
2. 如果输入不在 1-100 内:
   输出 "超出范围", 不消耗次数, 继续下一轮.
3. 有效猜测消耗 1 次机会:
   猜小了, 输出 "猜小了";
   猜大了, 输出 "猜大了";
   猜对了, 输出 "猜对了, 共用了 X 次", 立即结束循环.
4. 猜错且还有机会时, 输出剩余次数.
5. 5 次机会用完仍未猜对:
   输出 "机会已用完, 正确答案是 X".
6. 猜对后不能再输出失败提示.

要求:
使用 while, if / elif / else, continue, break.
不使用列表或自定义函数.

检查:
输入 0: 不消耗机会.
输入 30, 80, 67: 第 3 次猜中.
连续猜错 5 次: 输出失败提示.
第 5 次恰好猜中: 只输出成功提示.
"""

# from re import I


# answer = 67  # answer: 正确答案
# attempts = 0  # attempts: 已使用的次数
# limit = 5  # limit: 次数上限
# won = False;

# # input("请输入猜测值: ") 获取输入, 返回字符串.
# # int(...) 将输入的字符串转换成整数.

# while attempts < limit:
#     guessed = int (input("猜数字："))

#     attempts += 1   #猜一次计数一次

#     if guessed < 1 or guessed > 100:
#         print("超出范围请重试")
#         continue;   #超出范围


#     if guessed != answer:
#         print("答案错误请重试")

#         if guessed > answer:
#             print("猜大了")
#             continue;

#         if guessed < answer:
#             print("猜小了")
#             continue;   #数字比较
        
#     elif guessed == answer:
#         print("答案正确")
#         won = True
#         break;
# if won == False:
#     print (f"机会已用完,正确答案是{answer}")
# else:
#     print (f"恭喜你答对了,你一共猜了{attempts}次")
"""
写了好几版,学cpp的时候也卡在这个
"""
