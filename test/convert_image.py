from PIL import Image
import numpy as np

# 打开一张图片
img = Image.open("image/张三.png")
# 图片灰度化
img = img.convert("L")
# 显示图片
img.show()
# 将图片转换为数组形式，元素为其像素的亮度值
print(np.asarray(img))