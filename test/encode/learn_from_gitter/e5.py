import io
import av


def encode_frames(self, calculate_bitrate: bool, options: dict) -> bytes:
    """Encodes frames and returns movie buffer

    Args:
        calculate_bitrate (bool)
        options (dict): [extra options for av library]

    Returns:
        [bytes]: [movie buffer]
    """
    container = "mp4"
    frames = self.all_frames()
    if not frames:
        return bytes()
    mp4_bio = io.BytesIO()
    mp4_bio.name = f"out.{container}"
    new_options = options.copy()
    new_options["video_track_timescale"] = str(self._samplerate)
    mp4_container = av.open(
        mp4_bio,
        mode="w",
        format=container,
        options=new_options
    )
    self._bio.seek(0)
    with av.open(self._bio, mode="r") as video_in:
        in_stream = video_in.streams.video[0]
        stream = mp4_container.add_stream("h264", self.FPS)
        stream.pix_fmt = "yuvj420p"
        stream.extradata = in_stream.extradata
        stream.bit_rate = in_stream.bit_rate
    stream.width = frames[0].shape[1]
    stream.height = frames[0].shape[0]
    for i, frame in enumerate(frames):
        format = "rgb24" if frame.ndim >= 3 else "gray"
        video_frame = av.VideoFrame.from_ndarray(frame, format=format)
        for packet in stream.encode(video_frame):
            mp4_container.mux(packet)
    if i >= 0:
        for p in stream.encode(None):
            mp4_container.mux(p)
    mp4_container.close()
    return mp4_bio.getvalue()