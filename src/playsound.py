import pysinewave as sound
import pysinewave.utilities
import time
import threading

PPS = 100000 # Controls the maximum change in pich per second, an arbitrarily large number.
DPS = 1000 # Controls the maximum change in volume per second.



class Sound():
    def __init__(self,frequency):
        self.frequency = frequency
        self.sinewave = sound.SineWave(pitch_per_second=PPS, decibels_per_second=DPS)
        self.sinewave.set_frequency(frequency)

    def start(self):
        "Starts the sound"
        self.sinewave.play()

    def stop(self):
        """Stops the sound gracefully without causing a popping noice. 
        This takes about 2.5 milliseconds. If you want an immidiate stop, use force_stop()"""
        self.sinewave.sinewave_generator.set_amplitude(0)
        time.sleep(0.1)
        self.sinewave.stop()

    def force_stop(self):
        """Stop the sound forcefully. 
        WARNING! This will likely lead to a popping/clicking sound.
        I'd suggest you to use the stop() function."""
        self.sinewave.stop()