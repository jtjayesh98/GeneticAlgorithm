import numpy as np

def avg_mutator(score1, score2):
    if (score1 + score2)/2 > 1:
        return score1
    else:
        return (score1+score2)/2

def add_mutator(score1, score2):
    if score1 + score2 > 1:
        return score2
    else:
        return score1 + score2

def sub_mutator(score1, score2):
    return np.abs(score1-score2)

def one_mutator(score1, score2):
    return 1

def zero_mutator(score1, score2):
    return 0

def first_mutator(score1, score2):
    return score1

def second_mutator(score1, score2):
    return score2

def dominant_mutator(score1, score2):
    if score1 > score2:
        return score1
    else:
        return score2

def random_mutation(score1, score2):
    return np.random.rand(1)

def mutator(score1, score2, object):
    probability = [0.01, 0.01, 0.01, 0.06, 0.06, 0.2, 0.2, 0.4, 0.05]
    
    mutation = np.random.choice(range(9), 1, p = probability)
    if mutation == 0:
        return avg_mutator(score1, score2)
    elif mutation == 1:
        return add_mutator(score1, score2)
    elif mutation == 2:
        return sub_mutator(score1, score2)
    elif mutation == 3:
        return one_mutator(score1, score2)
    elif mutation == 4:
        return zero_mutator(score1, score2)
    elif mutation == 5:
        return first_mutator(score1, score2)
    elif mutation == 6:
        return second_mutator(score1, score2)
    elif mutation == 7:
        return dominant_mutator(score1, score2)
    elif mutation == 8:
        return float(random_mutation(score1, score2))