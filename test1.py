import cv2
import numpy as np
import matplotlib.pyplot as plt


def letterbox_image(image, size):
    ih, iw, _ = np.shape(image)  # 获取原始图像的高度、宽度和通道数
    w, h = size  # 获取目标大小的宽度和高度
    scale = min(w / iw, h / ih)  # 计算缩放比例，选择宽度和高度的最小比例，以确保图像在指定大小的画布内完全显示
    nw = int(iw * scale)  # 计算缩放后的图像宽度
    nh = int(ih * scale)  # 计算缩放后的图像高度

    image_resized = cv2.resize(image, (nw, nh))  # 使用 OpenCV 的 cv2.resize() 函数将图像按照计算得到的新宽度和高度进行缩放
    new_image = np.ones([h, w, 3]) * 128  # 创建一个指定大小的画布，并将其填充为灰色（RGB 值为 [128, 128, 128]）
    new_image[(h - nh) // 2: (h - nh) // 2 + nh,
    (w - nw) // 2: (w - nw) // 2 + nw] = image_resized  # 将缩放后的图像放置在画布中心。如果图像的缩放后尺寸小于目标大小，则在画布中心填充灰色背景

    return new_image  # 返回处理后的图像，即放置在指定大小画布中心的图像


# 加载示例图像
image_path = 'img/zhangxueyou.jpg'  # 替换为你的图像路径
image = cv2.imread(image_path)

# 目标尺寸
target_size = (300, 300)

# 调用函数进行处理
letterboxed_image = letterbox_image(image, target_size)

# 可视化处理前后的图像
plt.figure(figsize=(10, 5))

# 原始图像
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Letterbox处理后的图像
plt.subplot(1, 2, 2)
plt.title("Letterboxed Image")
plt.imshow(cv2.cvtColor(letterboxed_image.astype(np.uint8), cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
