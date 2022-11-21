import av
from pathlib import Path


video_dir = f"{Path(__file__).parent.parent}/video"
video = f"{video_dir}/test_5.mp4"
# https://pyav.org/docs/stable/api/container.html
container = av.open(video)
print(container.duration)
print(container.bit_rate)
print(container.size)

# https://pyav.org/docs/stable/api/container.html#av.format.ContainerFormat
print(container.format)
print(container.format.name)
print(container.format.long_name)
print(container.format.options)
print(container.format.input)
print(container.format.output)

# https://pyav.org/docs/stable/api/container.html#av.container.OutputContainer
# https://pyav.org/docs/stable/api/container.html#av.container.InputContainer.seek
# https://pyav.org/docs/stable/api/video.html?highlight=to_ndarray#module-av.video.stream
stream = container.streams.video[0]
audio_stream = container.streams.audio[0]
print(container.streams)
print(container.streams.video)
print(type(container.streams.video))
print(container.streams.audio)
print(audio_stream)
print(stream)
# https://pyav.org/docs/stable/api/stream.html#av.stream.Stream
print(stream.time_base)
print(stream.start_time)
print(stream.duration)
print(stream.frames)
print(stream.bit_rate)
print(stream.codec_context.format)
print(stream.codec_context.coded_height)
print(stream.codec_context.coded_width)
print(stream.codec_context.height)
print(stream.codec_context.width)
print(stream.codec_context.framerate)
print(type(stream.codec_context.framerate))
print(stream.codec_context.display_aspect_ratio)
print(stream.codec_context.gop_size)
print(stream.codec_context.has_b_frames)
print(stream.codec_context.pix_fmt)
print(stream.codec_context.rate)
print(stream.codec_context)
print(stream.duration)


print("-"*156)
# https://gitter.im/PyAV-Org/User-Help?at=62bc61a476cd751a2f8a3b42
print(av.codecs_available)