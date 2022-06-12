import numpy as np
from evaluation import evaluation_generation, evaluation_individual
from populator import generation
from mutator import mutator

# Calculates the maximum value in a given list. Used for finding the best score in a given population.
def max(list):
    return np.max(list)

# Calculates the final sum of the list. Used in the calculation of the softmax function
def sum(list):
    return np.sum(list)

# Calculates the minimum value in a given list.
def min(list):
    return np.min(list)

# Calcaluate the Probability of a given individual to be chosen as a parent in a given population, based on their evaluation score. 
''' Rename Sigmoid to Softmax '''
def sigmoid(list):
    output_list = []
    for x in list:
        output_list.append(np.exp(x))
    sum_list = sum(output_list)
    output_list = output_list/sum_list
    return output_list

# Gets two parent individuals from a given population.
def parents(population, problem):
    scores = evaluation_generation(population, problem)
    probability = sigmoid(scores)
    parents = np.random.choice(range(len(population.population)), 2, replace = False, p = probability)
    return (population.population[parents[0]], population.population[parents[1]])

# Creates the offspring in a given population, based on the parent generated.
def offspring(parents, problem):
    numGenes = len(parents[0])
    offSpring = []
    for i in range(numGenes):
        score1 = parents[0][i]
        score2 = parents[1][i]
        object = problem.object_list[i]
        offSpring.append(mutator(score1, score2, object))
    return offSpring

# Creates multiple offsprings and generates the next generation. 
def next_generation(population, problem):
    offsprings = []
    for i in range(1000):
        offsprings.append(offspring(parents(population, problem), problem))
    nextGeneration = generation(offsprings)
    return nextGeneration