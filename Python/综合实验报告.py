import requests
import re
import openpyxl
import matplotlib.pyplot as plt

# 解决matplotlib中文显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def crawl_power_data():
    # 1. 爬取网页文本内容
    url = "https://www.hxny.com/nd-102461-0-17.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        page_text = response.text
    except Exception as e:
        print(f"网页爬取失败：{e}")
        return None

    # 2. 用正则提取省份+2024年3月总发电量
    # 正则规则：匹配"2024年3月，XX总发电量XX亿千瓦时"的结构
    power_pattern = re.compile(r'2024年3月，([\u4e00-\u9fa5]+)总发电量([\d.]+)亿千瓦时')
    data = power_pattern.findall(page_text)  # 返回列表，每个元素是(省份, 发电量)
    
    # 格式化数据（转为[省份, 发电量]的列表）
    formatted_data = [[province, f"{power}亿千瓦时"] for province, power in data]
    return formatted_data

def save_to_excel(data, filename="省份3月发电量数据.xlsx"):
    # 3. 保存到Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "2024年3月发电量"
    ws.append(["省份", "2024年3月总发电量"])
    for row in data:
        ws.append(row)
    wb.save(filename)
    print(f"数据已保存到{filename}")

def draw_bar_chart(data):
    # 4. 绘制柱状图
    provinces = [row[0] for row in data]
    # 提取发电量数值（去除"亿千瓦时"）
    powers = [float(row[1].replace("亿千瓦时", "")) for row in data]
    
    plt.figure(figsize=(14, 7))
    plt.bar(provinces, powers, color="#2ca02c")
    plt.title("2024年3月各省份总发电量分布")
    plt.xlabel("省份")
    plt.ylabel("总发电量（亿千瓦时）")
    plt.xticks(rotation=60, ha="right")  # 省份名旋转防重叠
    plt.tight_layout()
    plt.savefig("2024年3月省份发电量柱状图.png")
    plt.show()
    print("柱状图已生成并保存")

if __name__ == "__main__":
    data = crawl_power_data()
    if data:
        print("提取到的数据：", data)  # 调试用，可删除
        save_to_excel(data)
        draw_bar_chart(data)