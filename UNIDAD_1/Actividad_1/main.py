from src.signals import sinusoidal, exponential_step, triangular, square
from src.graphs import graphs
import numpy as np

def main():
    # Discretización
    t_cont = np.linspace(-1, 5, 1000)
    Ts = 0.05
    t_disc = np.arange(-1, 5 + Ts, Ts)
    
    # Señales
    signals = {
        "x₁(t) = sin(2π·f·t) (f=2Hz)": sinusoidal,
        "x₂(t) = e^(–2t) · u(t)*": exponential_step,
        "x₃(t) = tri(t, f) (f=2Hz)": triangular,
        "x₄(t) = sq(t, f) (f=2Hz)": square
    }
    
    # Graficas
    for title, func in signals.items():
        x_cont = func(t_cont)
        x_disc = func(t_disc)
        graphs(t_cont, x_cont, t_disc, x_disc, title)

if __name__ == "__main__":
    main()
