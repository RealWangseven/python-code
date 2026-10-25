"""
练习: 把文字成绩转换成整数列表

任务:
1. 用 split() 按逗号拆分 text, 保存到 parts.
2. 创建空列表 scores.
3. 遍历 parts, 把每项用 int() 转成整数,
   再添加到 scores.
4. 输出 scores.
5. 计算平均分, 输出时保留两位小数.

要求:
本题不用定义函数.
可以使用 sum() 和 len().
"""

# text = "72,85,59,90,66"  # text: 原始成绩文字

# # parts: 拆分后的字符串列表
# # scores: 转换后的整数列表
# # 请在下面编写代码:

# parts = text.split(",")
# scores = []

# for i in parts:
#     scores.append(int(i));

# print(scores)

# average = sum(scores) / len(scores)
# print(f"{average:.2f}")

"""
练习: 清理姓名列表

任务:
1. 按逗号拆分 text.
2. 用 strip() 去掉每个姓名两端的空格.
3. 清理后若为 "", 就跳过.
4. 将非空姓名添加到 names.
5. 输出姓名列表和人数.

要求:
不用定义函数.
保留姓名中间的空格.
"""

# text = "  Alex , Emma, , Mary Jane ,   "  # text: 原始姓名文字
# names = []  # names: 清理后的姓名列表

# # parts: 拆分结果
# # name: 当前姓名
# # clean: 清理后的姓名
# # 请在下面编写代码:

# parts = text.split(",")

# for name in parts:
#     clean = name.strip()
#     if clean == "":
#         continue
#     names.append(clean)
# print(names)
# print(len(names))

"""
练习: 整理语言名称

任务:
1. 按逗号拆分 text.
2. 去掉每项两端的空格, 跳过空字符串.
3. 把清理后的名称保存到列表 languages.
4. 用 " / " 连接列表中的名称, 保存到 output.
5. 输出 output 和名称个数.

期望显示格式:
Python / CPP / Java

要求:
保留名称中间的空格.
本题不定义函数.
"""



# text = " Python, CPP , , Java, C Sharp , "  # text: 原始文字
# languages = []  # languages: 清理后的语言名称列表

# # output: 拼接后的文字
# # 请在下面编写代码:

# parts = text.split(",")
# for name in parts:
#     clean = name.strip()
#     if clean == "":
#         continue;

#     languages.append(clean)
# output = " / ".join(languages)
# print(output)
# print(len(languages))

"""
练习: 整理文件名

任务:
1. 去掉 filename 两端的空格.
2. 将中间所有空格替换为下划线 "_".
3. 将 ".txt" 替换为 ".csv".
4. 输出最终文件名.
5. 输出原始 filename, 确认它没有改变.

要求:
使用 strip() 和 replace().
本题只处理字符串, 不操作实际文件.
"""

# filename = "  monthly sales report.txt  "  # filename: 原始文件名

# # cleaned: 去掉两端空格后的文字
# # output: 最终文件名
# # 请在下面编写代码:

# cleaned = filename.strip()
# replaced = cleaned.replace(" ","_")
# output = replaced.replace(".txt",".csv")
# print(filename)

"""
练习: 判断退出指令

任务:
1. 去掉 command 两端的空格.
2. 将它转换成小写.
3. 如果结果为 "quit" 或 "exit", 输出 "Goodbye".
4. 否则输出 "Unknown command".

要求:
先不使用 input() 或循环.
分别修改 command, 测试下面三个值:
"  QUIT  "
"Exit"
"hello"
"""


# command = "  QUIT  "  # command: 指令文字

# # cleaned: 清理并转小写后的指令
# # 请在下面编写代码:

# cleaned = command.strip()
# final = cleaned.lower()
# if final == "quit" or final == "exit":
#     print("Goodbye");
# else:
#     print("Unknown command");

"""
练习: 搜索课程名称

任务:
1. 遍历 courses.
2. 忽略大小写, 找出名称中包含 "python" 的课程.
3. 将符合条件的原始课程名称添加到 result.
4. 输出结果列表和课程数量.

要求:
使用 lower() 和 in.
保留课程名称原来的大小写.
"""




# courses = ["Python Basics", "CPP Basics", "PYTHON Practice", "Java Web"]
# # courses: 课程名称列表
# result = []  # result: 匹配到的课程列表

# # course: 当前课程名称
# # 请在下面编写代码:

# for i in courses:
#     if "python" in i.lower():
#         result.append(i)

# print(result)
# print(len(result))
    
"""
练习: 筛选 Python 文件名

任务:
1. 遍历 files.
2. 忽略大小写, 找出以 ".py" 结尾的文件名.
3. 把符合条件的原始文件名添加到 result.
4. 输出结果列表和数量.

注意:
"old.py.txt" 不符合要求, 因为它以 ".txt" 结尾.
保留文件名原来的大小写.
本题只处理文字, 不读取实际文件.
"""

# files = ["main.py", "notes.txt", "TEST.PY", "old.py.txt", "utils.py"]
# # files: 文件名列表
# result = []  # result: 筛选结果

# # filename: 当前文件名
# # 请在下面编写代码:

# for name in files:
#     if name.lower().endswith(".py"):
#         result.append(name);

# print(result,len(result));