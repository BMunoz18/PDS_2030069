import numpy as np

# Continuous Signal
def continuous_sin():
    frequency = 1
    amplitude = 1
    start_time = 0
    end_time = 5
    points = 5000
    t = np.linspace(start_time, end_time, points)
    x_t = amplitude * np.sin( 2 * np.pi * frequency * t )
    return t, x_t


# Discretization
def discrete_sin():
    frequency = 1
    amplitude = 1
    fs = 20
    ts = 1 / fs
    samples = 100
    n = np.arange(0,samples)
    x_n = amplitude * np.sin( 2 * np.pi * frequency * n * ts )
    return n, ts, x_n
