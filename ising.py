"""Basic Ising Model storing current state."""
import random as ran
import numpy as np

class Ising():
    """Wrapper class storing state, temperature, structure of Ising Model."""

    def __init__(self, length=10, beta=1.0, coupling=1.0):
        """By default, create line of 10 spins at beta=1."""
        assert(isinstance(length, int))
        self.length = length
        self.beta = beta
        self.coupling = coupling
        # initialize to random line state
        self.config = [ran.choice([-1, 1]) for _ in range(self.length)]
        # TODO Calculate DOS

    def energy(self):
        """Calculate Energy for the internal configuration."""
        return self.config_energy(self.config)

    def config_energy(self, config):
        """Calculate the Energy of a configuration."""
        e = 0
        for (i, s) in enumerate(self.config):
            e += self.coupling * self.config[i] * self.config[i-1]
        return e


    def calc_dos(self):
        """Calculate the density of states using Wang-Landau."""
        energy_min = -self.coupling*self.length
        energy_max = self.coupling*self.length
        d_energy = 1
        N = (energy_max - energy_min) / d_energy
        entropy_mat = np.zeros(N)
        f = 1.0
        while f > 1e-5:  # epsilon set here
            # Propose configuration
            sample_config = [ran.choice([-1, 1]) for _ in range(self.length)]
            sample_energy = self.config_energy(sample_config)
            if ran.random() < np.exp(

