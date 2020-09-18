#[Neural Network]

neural_network = {

    'size': [768, 180, 60, 1], 
    'activation function': 'sigmoid'

}

#[MinMax]

minmax = {

    'depth': 3

}

#[Population]

population = {

    'population size': 500

}

#[Genetic Algorithm]

genetic_algorithm = {
    
    'random start': 'random uniform',

    'parents number': 40,
    'parents selection type': 'roulette wheel', 

    'simulated binary crossover probability': 0.5,
    'uniform binary crossover probability': 0.1,
    'single point crossover probability': 0.4,

    'simulated binary crossover eta': 100,
    'single point crossover orientation': 'rows',

    'mutation probability': 0.015,
    'random uniform mutation probability': 0.5,
    'gaussian mutation probability': 0.5,
    'gaussian mutation scale': 0.2

}