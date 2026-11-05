import os

print(os.getcwd())  # 获取当前工作目录
print(os.listdir("."))  # 列出当前目录的文件和文件夹

print(os.path.exists("notes.txt"))  # 判断路径是否存在
print(os.path.isfile("notes.txt"))  # 判断是否为文件
print(os.path.isdir("data"))  # 判断是否为文件夹

path = os.path.join("data", "notes.txt")  # path: 拼接后的路径
print(path)

os.makedirs("data", exist_ok=True)  # 创建目录, 已存在也不报错
os.chdir("data")  # 改变当前工作目录, 影响后续相对路径

os.rename("old.txt", "new.txt")  # 重命名文件
os.remove("unused.txt")  # 删除文件, 不会放进废纸篓
os.rmdir("empty_folder")  # 删除空目录

key = os.getenv("OPENAI_API_KEY")  # key: 密钥; 未设置时得到 None