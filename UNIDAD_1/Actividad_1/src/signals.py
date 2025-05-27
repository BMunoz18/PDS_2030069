import numpy as np
from scipy import signal

def sinusoidal(t, f=2):   # Seno
    return np.sin(2 * np.pi * f * t)

def exponential_step(t):  #ExpoEsc
    return np.exp(-2 * t) * np.heaviside(t, 1)

def triangular(t, f=2):   #Tran
    return signal.sawtooth(2 * np.pi * f * t, width=0.5)

def square(t, f=2):       #Cuad
    return signal.square(2 * np.pi * f * t)
