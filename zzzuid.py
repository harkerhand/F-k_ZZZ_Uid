import pyautogui
import schedule
import time
import random

#  1220 960
#  930 930

# 指定位置的中心点
x_center = 1075
y_center = 945

# 随机范围（像素）
range_x = 145
range_y = 15

# 点击函数
def click():
    # 生成随机的点击位置
    x = x_center + random.randint(-range_x, range_x)
    y = y_center + random.randint(-range_y, range_y)
    pyautogui.click(x, y)
    print(f"Clicked at ({x}, {y})")

# 定时任务，每隔10秒点击一次
schedule.every(4).seconds.do(click)

while True:
    schedule.run_pending()
    time.sleep(1)
