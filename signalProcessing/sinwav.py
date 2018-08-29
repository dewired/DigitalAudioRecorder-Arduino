# -*- coding: utf-8 -*-

import numpy as np

import wave

import struct 

import matplotlib.pyplot as plt

frequency = 1000

numSamples = 48000

samplingRate = 48000.0

amplitude = 16000

file = "test.wav"

sine_wave = [np.sin(2 * np.pi * frequency * x/samplingRate) for x in range(numSamples)]

nframes=numSamples
 
comptype="NONE"
 
compname="not compressed"
 
nchannels = 1
 
sampwidth = 2

wav_file=wave.open(file, 'w')
 
wav_file.setparams((nchannels, sampwidth, int(samplingRate), nframes, comptype, compname))

for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))
   
