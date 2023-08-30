#!~/../venv/bin/python3

import pysinewave as sound

class Sound():
    def __init__(self,frequency):
        self.frequency = frequency
        self.sinewave = sound.SineWave(pitch_per_second=0)
        self.sinewave.set_frequency(frequency)
    def start(self):
        "Start the sound"
        self.sinewave.play()
    def stop(self):
        "Stop the sound"
        self.sinewave.stop()