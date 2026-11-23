# -*- coding: utf-8 -*-
"""读一个 CSV，打印行数与均值，并画一张图。
用法：python read_csv.py sample.csv
说明：零基础入门脚本，用于验证"数据能读进来、能出图"这条链路。
"""
import csv
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "sample.csv"

rows = []
with open(path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append(r)

print("文件:", path)
print("列名:", list(rows[0].keys()))
print("行数:", len(rows))

# 取第二列做均值（假设是数值列）
key = list(rows[0].keys())[1]
vals = [float(r[key]) for r in rows if r[key] not in ("", None)]
print("列 '%s' 的均值: %.3f" % (key, sum(vals) / len(vals)))

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.plot(vals, marker="o")
    plt.xlabel("sample #")
    plt.ylabel(key)
    plt.title("first look at " + key)
    plt.savefig("preview.png", dpi=120)
    print("已保存图: preview.png")
except ImportError:
    print("未安装 matplotlib，跳过画图（pip install matplotlib）")
