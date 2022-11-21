import av
from video_path import video, audio


# https://gitter.im/PyAV-Org/User-Help?at=62bc61a476cd751a2f8a3b42
class BatchAudioLoader:
    def __init__(self, sample_rate=16000, layout='mono', output_format='flt', output_planar=False):
        self._output_format = f'{output_format}{"p" if output_planar else ""}'
        self.resampler = av.audio.resampler.AudioResampler(self._output_format, layout, sample_rate)

    def post_process(self, audio):
        self.resampler.resample(None)
        return self.resampler.resample(audio)[0]

    def load(self, filename):
        buffer = av.audio.fifo.AudioFifo()
        with av.open(filename) as source:
            for frame in source.decode(source.streams.audio[0]):
                buffer.write(frame)
        whole_audio = buffer.read(0)
        if isinstance(whole_audio, list):
            whole_audio = whole_audio[0]
        whole_audio = self.post_process(whole_audio)
        sample_rate = whole_audio.sample_rate
        audio_arr = whole_audio.to_ndarray(format=self._output_format)
        return audio_arr, sample_rate


loader = BatchAudioLoader(sample_rate=16000)
# loader.load('file1')
# loader.load('file2')
loader.load(audio)
