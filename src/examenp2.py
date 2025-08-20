import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def dft2():
    fs = 256   
    Ts = 1 / fs  
    duration = 6  
    N = int(fs * duration)
    n = np.arange(N)
    f1 = 8
    f2 = 20

    x_n = np.sin(2 * np.pi * f1 * n * Ts) + 0.5 * np.sin(2 * np.pi * f2 * n * Ts)

    continuous_plotter(n * Ts, x_n, "Señal Original", "x[n]", "Tiempo [s]", "Amplitud")

    #ruido
    f_noise = 50
    noise = 0.5 * np.sin(2 * np.pi * f_noise * n * Ts)
    x_n_noise = x_n + noise

    continuous_plotter(n * Ts, x_n_noise, "Señal con Ruido", "x[n]+ruido", "Tiempo [s]", "Amplitud")

    X = np.fft.fft(x_n)
    X_noise = np.fft.fft(x_n_noise)
    freqs = np.fft.fftfreq(N, Ts)
    half = N // 2  
    discrete_plotter(freqs[:half], np.abs(X[:half]), "DFT Señal Original", "Amplitud DFT", "Frecuencia [Hz]", "Amplitud")

    discrete_plotter(freqs[:half], np.abs(X_noise[:half]), "DFT Señal con Ruido", "Amplitud DFT", "Frecuencia [Hz]", "Amplitud")

    delta_f = fs / N
    print(f"Resolución de frecuencia Δf = {delta_f:.4f} Hz")
