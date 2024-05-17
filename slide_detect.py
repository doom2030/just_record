import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_gap(background_img_path, slider_img_path):
    # 读取背景图片和滑块图片
    background = cv2.imread(background_img_path, 0)
    slider = cv2.imread(slider_img_path, 0)

    # 边缘检测
    background_edges = cv2.Canny(background, 100, 200)
    slider_edges = cv2.Canny(slider, 100, 200)

    # 使用模板匹配找到滑块缺口
    result = cv2.matchTemplate(background_edges, slider_edges, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果的最大值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 缺口位置的左上角
    top_left = max_loc
    bottom_right = (top_left[0] + slider.shape[1], top_left[1] + slider.shape[0])

    # 在背景图上绘制矩形标出缺口位置
    background_with_rectangle = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(background_with_rectangle, top_left, bottom_right, (0, 255, 0), 2)

    # 使用Matplotlib显示结果
    plt.figure(figsize=(10, 6))
    plt.imshow(background_with_rectangle, cmap='gray')
    plt.title('Detected Gap')
    plt.axis('off')
    plt.show()

    # 返回缺口的x坐标
    return top_left[0]

# 使用该函数，传入背景图片和滑块图片的路径
gap_x = find_gap('b.jpg', 't.jpg')
print(f"缺口位置的x坐标: {gap_x}")
