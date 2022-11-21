import av
import numpy as np

output_url = "rtmp://server.hu/main/test_input"
input_url = 'rtmp://server.hu/main/192.168.1.104'
container_in = av.open(input_url)
container_out = av.open(output_url, format='flv', mode='w')

video_stream_input = container_in.streams.video[0]
audio_stream_input = container_in.streams.audio[0]

video_stream_output = container_out.add_stream(template=video_stream_input)
audio_stream_output = container_out.add_stream(template=audio_stream_input)
# stream.width = 480
# stream.height = 320
video_stream_output.width = container_in.streams.video[0].codec_context.width
video_stream_output.height = container_in.streams.video[0].codec_context.height
video_stream_output.pix_fmt = container_in.streams.video[0].codec_context.pix_fmt
# audio_stream = container.add_stream(codec_name="aac", rate=16000)
the_canvas = np.zeros((video_stream_output.height, video_stream_output.width, 3), dtype=np.uint8)
the_canvas[:, :] = (32, 32, 32)  # some dark gray background because why not
my_pts = 0

while True:
    packet = next(container_in.demux(video_stream_input, audio_stream_input), None)

    # packet = None
    if packet is None:
        print("stream is not running")
        # TODO static black image
    else:
        if packet.stream.type == 'video':
            packet.stream = video_stream_output
            container_out.mux(packet)
        elif packet.stream.type == 'audio':
            packet.stream = audio_stream_output
            container_out.mux(packet)
