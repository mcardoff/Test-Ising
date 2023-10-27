"""Ising Model Simulation based on wikipedia article.

https://en.wikipedia.org/wiki/Monte_Carlo_method_in_statistical_mechanics.

"""
import matplotlib.pyplot as plt
import numpy as np

def main():
    """Initialize Ising Model, and start updating process."""
    # Below critical temperature (e.g., T = 2.0)
    simulate_ising_model(N=50, T=2.0, num_steps=1000)
    plt.show()
    # Above critical temperature (e.g., T = 3.0)
    # simulate_ising_model(N=50, T=3.0, num_steps=5000)
    # plt.show()
    # print('Hello World!')


def initialize_spin_lattice(N):
    return np.random.choice([-1, 1], size=(N, N))

def metropolis(spin_lattice, beta):
    N = spin_lattice.shape[0]
    for _ in range(N**2):
        i, j = np.random.randint(0, N, 2)
        dE = 2 * spin_lattice[i, j] * (
            spin_lattice[(i + 1) % N, j] +
            spin_lattice[(i - 1) % N, j] +
            spin_lattice[i, (j + 1) % N] +
            spin_lattice[i, (j - 1) % N]
        )
        if dE < 0 or np.random.rand() < np.exp(-beta * dE):
            spin_lattice[i, j] *= -1

def calculate_average_spin(spin_lattice):
    return np.mean(spin_lattice)

def plot_spin_lattice(spin_lattice, step, T):
    average_spin = calculate_average_spin(spin_lattice)
    plt.clf()
    plt.imshow(spin_lattice, cmap='coolwarm', interpolation='nearest')
    plt.title(f'Step {step}, Average Spin: {average_spin:.2f}, Temperature: {T}')
    plt.pause(0.01)

def simulate_ising_model(N, T, num_steps):
    spin_lattice = initialize_spin_lattice(N)
    beta = 1 / T
    plt.ion() # turn on interactive mode for plotting
    for step in range(num_steps):
        metropolis(spin_lattice, beta)
        if step % 2 == 0: # show even steps
            plot_spin_lattice(spin_lattice, step, T)
    plt.ioff() # turn off interactive mode after simulation

if __name__ == "__main__":
    main()
