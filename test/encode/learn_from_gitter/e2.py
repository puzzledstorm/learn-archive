import fractions
from typing import Tuple
import av


def create_encoder_context(codec_name: str, width: int, height: int, bitrate: int) -> Tuple[av.CodecContext, bool]:
    codec = av.CodecContext.create(codec_name, "w")
    codec.width = width
    codec.height = height
    codec.bit_rate = bitrate
    codec.pix_fmt = "yuv420p"
    codec.framerate = fractions.Fraction(25, 1)
    codec.time_base = fractions.Fraction(1, 25)
    codec.options = {
        "profile": "baseline",
        "level": "31",
        "tune": "zerolatency"  # does nothing using h264_omx,
    }
    codec.open()
    return codec, codec_name == "h264_nvmpi"

# self.codec, self.codec_buffering = create_encoder_context(
#                     "h264_nvmpi", frame.width, frame.height, bitrate=self.target_bitrate
#                 )