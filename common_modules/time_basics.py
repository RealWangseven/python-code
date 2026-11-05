import time  # time: 时间模块

time.sleep(2)  # sleep: 暂停约 2 秒, 可以写 0.5

# 测量程序耗时
start = time.perf_counter()  # start: 开始时刻; perf_counter: 高精度计时
time.sleep(1)
elapsed = time.perf_counter() - start  # elapsed: 耗时, 单位为秒

print(f"耗时: {elapsed:.2f} 秒")

# 获取当前时间戳
timestamp = time.time()  # timestamp: 自 Unix 纪元起经过的秒数
print(timestamp)

# 显示本地时间
now = time.strftime("%Y-%m-%d %H:%M:%S")  # now: 格式化后的本地时间
print(now)

"""
| 格式符 | 含义 |
|---|---|
| `%Y`、`%m`、`%d` | 年、月、日 |
| `%H`、`%M`、`%S` | 时、分、秒 |
"""