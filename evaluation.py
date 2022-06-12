import numpy as np

def evaluation_individual(solution, problem):
    bag = problem.bag
    object_list = problem.object_list
    profit = 0
    weight = 0
    for i in range(len(solution)):
        weight = weight + object_list[i].weight*solution[i]
        profit = profit + object_list[i].profit*solution[i]
    
    if weight > bag:
        return 1
    else:
        return profit

def evaluation_generation(population, problem):
    scores = []
    for solution in population.population:
        scores.append(evaluation_individual(solution, problem))
    return scores

