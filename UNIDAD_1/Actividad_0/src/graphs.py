import matplotlib.pyplot as plt

def graphs(t, x_t, n, ts, x_n):
    # Continuous
    plt.subplot(3, 1, 1)
    plt.plot(t, x_t, 'r')
    plt.title('Continuous Signal 1Hz')
    plt.grid()

    # Discrete
    plt.subplot(3, 1, 2)
    plt.stem(n*ts, x_n, basefmt='k')
    plt.title('Discrete Signal 1Hz')
    plt.grid()

    # Continuous & discrete
    plt.subplot(3, 1, 3)
    plt.plot(t, x_t, 'r')
    plt.stem(n*ts, x_n, basefmt='k')
    plt.title('Continuous & Discrete graphs merged')
    plt.grid()

    plt.show()
