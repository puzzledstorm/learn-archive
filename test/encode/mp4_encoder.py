import os
import os.path as osp
import shutil
import time

import av
import uuid
from decoder import Decoder


class Encoder:
    def __init__(self):
        self.fps = None
        self.bit_rate = None
        self.width = None
        self.height = None

        self.container = None
        self.stream = None

    def init_container(self, encode_video):
        self.container = av.open(encode_video, mode='w', format='flv')
        self.stream = self.container.add_stream("h264", rate=self.fps)
        self.container.streams.video[0].thread_type = "AUTO"
        self.stream.width = self.width
        self.stream.height = self.height
        self.stream.bit_rate = self.bit_rate
        self.stream.pix_fmt = "yuv420p"

    def put_frame(self, np_array):
        frame = av.VideoFrame.from_ndarray(np_array, format='bgr24')
        for packet in self.stream.encode(frame):
            self.container.mux(packet)

    def pre_process(self, param_dic=None):
        pass

    def post_process(self):
        # Flush stream
        for packet in self.stream.encode():
            self.container.mux(packet)

        # Close the file
        self.container.close()
        print(f"encode complete")

    def set_parameter(self, in_video):
        with av.open(in_video) as container:
            stream = container.streams.video[0]
            self.fps = stream.codec_context.framerate  # type :Fraction
            self.width = stream.codec_context.width
            self.height = stream.codec_context.height
            self.bit_rate = stream.bit_rate  # video的码率
            # self.bit_rate = container.bit_rate  # 视频总码率

    def load(self, filename):
        pass

    def destroy(self):
        if self.container:
            self.container.close()
        self.container = None
        self.stream = None


def main():
    video = "video/test_5.mp4"
    if osp.exists("temp/"):
        shutil.rmtree("temp/")
        os.makedirs("temp/")
    temp_dir = f"temp/{str(uuid.uuid4()).replace('-', '')}/"
    if not osp.exists(temp_dir):
        os.makedirs(temp_dir)

    d = Decoder()

    # start_time = time.time()
    # frames = d.av_decoder(video)
    # encode_video = f"{temp_dir}av_encode.mp4"
    # self.av_set_parameter(video)
    # print(self.bit_rate)
    # self.av_encoder(frames, encode_video)
    # end_time = time.time()
    # print(f"av decode and encode time: {end_time - start_time}")

    try:
        e = Encoder()
        e.set_parameter(video)
        encode_video = f"{temp_dir}av_encode.mp4"
        e.init_container(encode_video)

        frames = d.av_decoder(video)
        for frame in frames:
            e.put_frame(frame)
        e.post_process()
        e.destroy()
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
