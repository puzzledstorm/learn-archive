"""
Destination: encode a video, only with video stream
Some documents：
http://ffmpeg.org/documentation.html

"""
import os
import os.path as osp
import shutil
import time

import cv2
import numpy as np
import av
import uuid
from decoder import Decoder


class Encoder(object):
    def __init__(self):
        super(Encoder, self).__init__()
        self.fps = 25
        self.width = 1920
        self.height = 1080
        self.bit_rate = 8 * 1014 * 1024

    def av_encoder(self, frames, encode_video):
        # 编码一个视频
        # duration = 4
        # fps = 24
        # total_frames = duration * fps
        #
        # container = av.open(encode_video, mode="w")
        #
        # stream = container.add_stream("mpeg4", rate=fps)
        # stream.width = 480
        # stream.height = 320
        # stream.pix_fmt = "yuv420p"
        #
        # for frame_i in range(total_frames):
        #
        #     img = np.empty((480, 320, 3))
        #     img[:, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + frame_i / total_frames))
        #     img[:, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + frame_i / total_frames))
        #     img[:, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + frame_i / total_frames))
        #
        #     img = np.round(255 * img).astype(np.uint8)
        #     img = np.clip(img, 0, 255)
        #
        #     frame = av.VideoFrame.from_ndarray(img, format="rgb24")
        #     for packet in stream.encode(frame):
        #         container.mux(packet)
        #
        # # Flush stream
        # for packet in stream.encode():
        #     container.mux(packet)
        #
        # # Close the file
        # container.close()

        # 编码一个视频返回
        # fps = 25
        container = av.open(encode_video, mode="w")
        stream = container.add_stream("mpeg4", rate=self.fps)
        container.streams.video[0].thread_type = "AUTO"
        stream.width = self.width
        stream.height = self.height
        stream.bit_rate = self.bit_rate
        stream.pix_fmt = "yuv420p"
        # stream.options = {"crf": "23"}

        for frame in frames:
            frame = av.VideoFrame.from_ndarray(frame, format="bgr24")
            for packet in stream.encode(frame):
                container.mux(packet)

        # Flush stream
        for packet in stream.encode():
            container.mux(packet)

        # Close the file
        container.close()
        print(f"{encode_video} encode complete")

    def cv2_encoder(self, frames, encode_video):
        size = (self.width, self.height)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # *'mp4v'
        out = cv2.VideoWriter(encode_video, fourcc, self.fps, size)
        for frame in frames:
            out.write(frame)
        out.release()
        print(f"{encode_video} encode complete")

    def av_set_parameter(self, video):
        with av.open(video) as container:
            stream = container.streams.video[0]
            self.fps = stream.codec_context.framerate  # type :Fraction
            self.width = stream.codec_context.width
            self.height = stream.codec_context.height
            self.bit_rate = stream.bit_rate  # video的码率
            # all_bit_rate = container.bit_rate  # 视频总码率

    def cv2_set_parameter(self, video):
        cap = cv2.VideoCapture(video)
        self.fps = int(round(cap.get(cv2.CAP_PROP_FPS)))  # 帧率
        self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 分辨率-宽度
        self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 分辨率-高度

        # frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   # 总帧数
        # https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
        # 2.4 can't find bit rate
        # https://docs.opencv.org/5.x/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        # find it, but my opencv version can't use it
        # self.bit_rate = int(cap.get(cv2.CAP_PROP_BITRATE))
        cap.release()

    def main(self):
        video = "video/test_5.mp4"
        if osp.exists("temp/"):
            shutil.rmtree("temp/")
            os.makedirs("temp/")
        temp_dir = f"temp/{str(uuid.uuid4()).replace('-', '')}/"
        if not osp.exists(temp_dir):
            os.makedirs(temp_dir)

        d = Decoder()

        start_time = time.time()
        frames = d.av_decoder(video)
        encode_video = f"{temp_dir}av_encode.mp4"
        self.av_set_parameter(video)
        print(self.bit_rate)
        self.av_encoder(frames, encode_video)
        end_time = time.time()
        print(f"av decode and encode time: {end_time - start_time}")

        start_time = time.time()
        frames = d.cv2_decoder(video)
        encode_video = f"{temp_dir}cv2_encode.mp4"
        self.cv2_set_parameter(video)
        print(self.bit_rate)
        self.av_encoder(frames, encode_video)
        end_time = time.time()
        print(f"cv2 decode and encode time: {end_time - start_time}")


if __name__ == '__main__':
    e = Encoder()
    e.main()
