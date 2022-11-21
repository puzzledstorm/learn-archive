# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread('messi5.jpg', 0)
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

from video_path import video_dir, video
import numpy as np
import cv2

#
# cap = cv2.VideoCapture(video)
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (640, 480))
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret:
#         # frame = cv2.flip(frame, 0)
#
#         # write the flipped frame
#         out.write(frame)
#
#         # cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()


cap = cv2.VideoCapture(video)
out_video = "out.mp4"
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))  # 帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 分辨率-宽度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 分辨率-高度
# frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   # 总帧数

# videowriter
# width = 1920
# height = 1080
# fps = 25
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # *'mp4v'
out = cv2.VideoWriter(out_video, fourcc, fps, size)

# read video
success, image = cap.read()
while success:
    success, image = cap.read()
    if success:
        x, y, w, h = 0, 0, 300, 300
        # 参数：pt1,对角坐标１, pt2:对角坐标２
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
        out.write(image)
        # print(image)
        # print(type(image))
    print('Read a new frame: ', success)
cap.release()
out.release()
