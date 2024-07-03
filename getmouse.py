import pyautogui
import time

try:
    while True:
        current_mouse_x, current_mouse_y = pyautogui.position()
        print(f"当前鼠标位置: ({current_mouse_x}, {current_mouse_y})")
        time.sleep(1)  # 每秒钟获取一次位置
except KeyboardInterrupt:
    print("监测已终止")


