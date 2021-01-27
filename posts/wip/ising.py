import numpy as np
from copy import deepcopy

class SpinModel():
    
    def __init__(self, dimensions, J, h, T):
        self.dimensions = dimensions
        self.spins = np.ones(self.dimensions)
        self.J = J
        self.h = h
        self.T = T
        self.N = np.prod(dimensions)
    
    def compute_local_field(self,index):
        ang = 0
        for dim in range(len(index)):
            p_index = list(index)
            p_index[dim] = (p_index[dim] + 1) % self.dimensions[dim]
            m_index = list(index)
            m_index[dim] = (m_index[dim] - 1) % self.dimensions[dim]
            ang += self.J*(self.spins[p_index] + self.spins[m_index])
        return self.h + ang

    def random_coordinate(self):
        return tuple([np.random.randint(d) for d in self.dimensions])
    
    def Magnetisation(self):
        return (1/self.N) * np.sum(self.spins)
    
    def Energy(self):
        ang = 0
        for i in range(len(spins)):
            ang += spins[i-1] * spins[i]

        entropy = self.h * np.sum(self.spins)
        return -1 * self.J * ang - entropy
    
    def update(self):

        index = self.random_coordinate()
        local_field = self.compute_local_field(index)
        r = np.random.rand()

        prob = 1/(1 + np.exp(-2*local_field/self.T))

        if r<prob:
            flipped_state = 1
        else:
            flipped_state = -1
            
        self.spins[index] = flipped_state

    
def run_simulation(spins, n_I, logging=False, save_output=False):
    N = spins.N
    for i in range(N * n_I):
        spins.update()
    return spins.Magnetisation()
    
def run_main(K, spins, warmup, n_I):
    mags = np.zeros(K)
    

    #warm up period
    for i in range(spins.N * warmup):
        spins.update()

    for k in range(K):
        mags[k] = run_simulation(spins, n_I)
    return mags
    
if __name__ == "__main__":
    pass