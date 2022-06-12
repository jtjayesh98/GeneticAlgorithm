import numpy as np
from evaluation import evaluation_individual, evaluation_generation
from populator import population
from crossover import sigmoid, max, min, parents, sum, offspring, next_generation


class object():
    def __init__(self, weight_, profit_):
        self.weight = weight_
        self.profit = profit_
    
class problem():
    def __init__(self, bag_, object_list_):
        self.bag = bag_
        self.num_object = len(object_list_)
        self.object_list = object_list_
class solution():
    def __init__(self, object_list_):
        self.x = np.random.rand(len(object_list_))


bag = 15

obj1 = object(2, 10)
obj2 = object(3, 5)
obj3 = object(5, 15)
obj4 = object(7, 7)
obj5 = object(1, 3)
obj6 = object(4, 18)
obj7 = object(1, 6)

object_list = []
object_list.append(obj1)
object_list.append(obj2)
object_list.append(obj3)
object_list.append(obj4)
object_list.append(obj5)
object_list.append(obj6)
object_list.append(obj7)

prob1 = problem(bag, object_list)
sol1 = solution(object_list)
pop1 = population(1000, object_list)

# offSpring = offspring(parents(pop1, prob1))

def iterator(population, problem):
    print(max(evaluation_generation(population, problem)))
    for i in range(100):
        population = next_generation(population, problem)
        print(max(evaluation_generation(population, problem)))
    return population

final_pop = iterator(pop1, prob1)
weight_sol = []
weight = 0
for i in final_pop.population:
    print(i)
# print(weight)
