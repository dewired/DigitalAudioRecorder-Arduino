#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:24:10 2018

@author: navani
"""

import numpy as np

import wave

import struct 

import matplotlib.pyplot as plt

frameRate = 24000.0

infile = "testfile.wav"

numSamples = 24000

wavFile = wave.open(infile, 'r')

data = wavFile.readframes(numSamples)

wavFile.close()

data = struct.unpack('{n}h'.format(n = numSamples), data)

data = np.array(data)

data_fft = np.fft.fft(data)

# This will give us the frequency we want
 
frequencies = np.abs(data_fft)

print("The frequency is {} Hz".format(np.argmax(frequencies)))

plt.subplot(2,1,1)
 
plt.plot(data[:300])
 
plt.title("Original audio wave")
 
plt.subplot(2,1,2)
 
plt.plot(frequencies)
 
plt.title("Frequencies found")
 
plt.xlim(0,1200)
 
plt.show()