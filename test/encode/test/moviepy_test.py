from moviepy.editor import *
from video_path import video

clip = VideoFileClip(video)
# clip.write_videofile("out.webm")

frames = [frame for frame in clip.iter_frames()]
print(len(frames))
