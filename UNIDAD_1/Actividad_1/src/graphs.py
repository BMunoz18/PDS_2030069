import matplotlib.pyplot as plt

def graphs(t_cont, x_cont, t_disc, x_disc, title):
    plt.figure(figsize=(8, 8))
    
    # Señal continua
    plt.subplot(3, 1, 1)
    plt.plot(t_cont, x_cont, 'r')
    plt.title(f'{title} - Continu')
    plt.grid()
    
    # Señal discreta
    plt.subplot(3, 1, 2)
    plt.stem(t_disc, x_disc, basefmt='k')
    plt.title(f'{title} - Discreta')
    plt.grid()
    
    # Señal continua y discreta superpuestas
    plt.subplot(3, 1, 3)
    plt.plot(t_cont, x_cont, 'r')
    plt.stem(t_disc, x_disc, basefmt='k')
    plt.title(f'{title} - Sobrepuestas')
    plt.grid()
    
    plt.tight_layout()
    plt.show()
