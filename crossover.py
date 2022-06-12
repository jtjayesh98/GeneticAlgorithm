import numpy as np
from evaluation import evaluation_generation, evaluation_individual
from populator import generation
from mutator import mutator

def max(list):
    return np.max(list)

def sum(list):
    return np.sum(list)

def min(list):
    return np.min(list)

def sigmoid(list):
    output_list = []
    for x in list:
        output_list.append(np.exp(x))
    sum_list = sum(output_list)
    output_list = output_list/sum_list
    return output_list

def parents(population, problem):
    scores = evaluation_generation(population, problem)
    probability = sigmoid(scores)
    parents = np.random.choice(range(len(population.population)), 2, replace = False, p = probability)
    return (population.population[parents[0]], population.population[parents[1]])

def offspring(parents, problem):
    numGenes = len(parents[0])
    genechoice = np.random.choice(range(2), numGenes)
    offSpring = []
    geneNum = 0
    for i in range(numGenes):
        score1 = parents[0][i]
        score2 = parents[1][i]
        object = problem.object_list[i]
        offSpring.append(mutator(score1, score2, object))
    return offSpring

def next_generation(population, problem):
    offsprings = []
    for i in range(1000):
        offsprings.append(offspring(parents(population, problem), problem))
    nextGeneration = generation(offsprings)
    return nextGeneration