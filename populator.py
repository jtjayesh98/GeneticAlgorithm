import numpy as np

class population():
    def __init__(self, size_, object_list_):
        self.population = []
        for i in range(size_):
            self.population.append(np.random.rand(len(object_list_)))

class generation():
    def __init__(self, offsprings):
        self.population = offsprings
        