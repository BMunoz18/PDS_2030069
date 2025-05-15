from src.signal import continuous_sin, discrete_sin
from src.graphs import graphs

def main():
    # Signal (Continuous % Discrete)
    t, x_t = continuous_sin()
    n, ts, x_n = discrete_sin()

    # Graphs
    graphs(t, x_t, n, ts, x_n)

if __name__ == "__main__":
    main()
