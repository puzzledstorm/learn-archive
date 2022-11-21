"""
Destination: decode a video, get all frames
Some documents：
http://ffmpeg.org/documentation.html

"""
import os
import os.path as osp
import shutil
import time
import uuid
import av
import cv2
from PIL import Image
import numpy as np


class Decoder(object):

    def __init__(self):
        super(Decoder, self).__init__()

    @staticmethod
    def av_decoder(path_to_video, frame_dir="frames/"):
        """
        PyAV document: https://pyav.org/docs/stable/index.html
        https://pyav.org/docs/stable/cookbook/numpy.html
        Returns:

        """
        # 解码所有帧
        # container = av.open(path_to_video)
        #
        # for frame in container.decode(video=0):
        #     image = f"{frame_dir}frame-%04d.jpg"
        #     frame.to_image().save(image % frame.index)

        # 解码关键帧
        # with av.open(path_to_video) as container:
        #     # Signal that we only want to look at keyframes.
        #     stream = container.streams.video[0]
        #     stream.codec_context.skip_frame = "NONKEY"
        #
        #     for frame in container.decode(stream):
        #         print(frame)
        #
        #         # We use `frame.pts` as `frame.index` won't make must sense with the `skip_frame`.
        #         image = frame_dir + "night-sky.{:04d}.jpg"
        #         frame.to_image().save(
        #             image.format(frame.pts),
        #             quality=80,
        #         )

        # 解码获取barcode
        # A video barcode shows the change in colour and tone over time.
        # Time is represented on the horizontal axis, while the vertical remains the vertical direction in the image.
        # container = av.open(path_to_video)
        # container.streams.video[0].thread_type = "AUTO"  # Go faster!
        #
        # columns = []
        # for frame in container.decode(video=0):
        #     print(frame)
        #     array = frame.to_ndarray(format="rgb24")
        #
        #     # Collapse down to a column.
        #     column = array.mean(axis=1)
        #
        #     # Convert to bytes, as the `mean` turned our array into floats.
        #     column = column.clip(0, 255).astype("uint8")
        #
        #     # Get us in the right shape for the `hstack` below.
        #     column = column.reshape(-1, 1, 3)
        #
        #     columns.append(column)
        #
        # # Close the file, free memory
        # container.close()
        #
        # full_array = np.hstack(columns)
        # full_img = Image.fromarray(full_array, "RGB")
        # full_img = full_img.resize((800, 200))
        # full_img.save(f"{frame_dir}barcode.jpg", quality=85)

        # 解码获取视频帧并转换np数组
        container = av.open(path_to_video)
        container.streams.video[0].thread_type = "AUTO"

        np_frames = []
        for frame in container.decode(video=0):
            print(frame)
            array = frame.to_ndarray(format="bgr24")
            np_frames.append(array)
        container.close()
        # print(np_frames)
        print(len(np_frames))
        print(np_frames[0].shape)
        return np_frames

    @staticmethod
    def cv2_decoder(path_to_video, frame_dir="frames/"):
        """
        opencv-python document: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
        https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
        Returns:

        """
        cap = cv2.VideoCapture(path_to_video)
        np_frames = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                # print("Can't receive frame (stream end?). Exiting ...")
                break
            print('read a new frame')
            np_frames.append(frame)
        cap.release()
        print(len(np_frames))
        print(np_frames[0].shape)
        return np_frames

    @staticmethod
    def moviepy_decoder(path_to_video, frame_dir="frames/"):
        """
        MoviePy document: https://zulko.github.io/moviepy/ref/ref.html

        https://zulko.github.io/moviepy/getting_started/quick_presentation.html
        ----
        And here are a few uses for which MoviePy is NOT the best solution:

        You only need to do frame-by-frame video analysis (with face detection or other fancy stuff).
        This could be done with MoviePy in association with other libraries, but really, just use imageio,
        OpenCV or SimpleCV, these are libraries that specialize in these tasks.

        You only want to convert a video file, or turn a series of image files into a movie.
        In this case it is better to directly call ffmpeg (or avconv or mencoder…)
        it will be faster more memory-efficient than going through MoviePy.

        Try after you will follow the author's advice
        https://zulko.github.io/moviepy/ref/videotools.html#moviepy.video.tools.subtitles.SubtitlesClip.iter_frames
        Returns:

        """
        from moviepy.editor import VideoFileClip
        clip = VideoFileClip(path_to_video)
        np_frames = [frame for frame in clip.iter_frames()]
        clip.close()
        print(len(np_frames))
        print(np_frames[0].shape)
        return np_frames

    def main(self):
        video = "video/test_5.mp4"
        if osp.exists("frames/"):
            shutil.rmtree("frames/")
            os.makedirs("frames/")
        frame_dir = f"frames/{str(uuid.uuid4()).replace('-', '')}/"
        if not osp.exists(frame_dir):
            os.makedirs(frame_dir)

        start_time = time.time()
        self.av_decoder(video, frame_dir)
        end_time = time.time()
        print(f"av decode time: {end_time - start_time}")

        start_time = time.time()
        self.cv2_decoder(video, frame_dir)
        end_time = time.time()
        print(f"cv2 decode time: {end_time - start_time}")

        start_time = time.time()
        self.moviepy_decoder(video, frame_dir)
        end_time = time.time()
        print(f"moviepy decode time: {end_time - start_time}")


if __name__ == '__main__':
    d = Decoder()
    d.main()
