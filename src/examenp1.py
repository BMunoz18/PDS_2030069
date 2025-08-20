import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def dft1():
    end_time = 2
    fm = 0.5   
    fc = 8     
    m = 0.5    
    t = np.linspace(0, end_time, 10000)
    x_t = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)
    continuous_plotter(t, x_t, "Señal AM continua", "continua", "Tiempo [s]", "Amplitud")

    fs = 100  
    n = np.arange(int(end_time * fs))
    x_n = (1 + m * np.cos(2 * np.pi * fm * n/fs)) * np.sin(2 * np.pi * fc * n/fs)
    discrete_plotter(n, x_n, "Señal AM discreta", "discreta", "Tiempo [n*ts]", "Amplitud")

    X = np.fft.fft(x_n)
    N = len(x_n)
    k = np.arange(N)
    discrete_plotter(k, np.abs(X), "Transformada de Fourier Discreta", "discreta", "k (índice de frecuencia)", "Amplitud")


    freqs = np.fft.fftfreq(N, 1/fs)
    discrete_plotter(freqs[:N//2], np.abs(X[:N//2]), "DFT AM (mitad positiva)", "discreta", "Frecuencia [Hz]", "Amplitud")
