from genetic_algorithm.populations import *
import pickle

population = newPopulation(random_start=True)
generation = 0

while True:

    generation += 1
    population.playGames(generation)

    best_individual = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
    with open("winner_network", "wb") as file:
        pickle.dump(best_individual[0], file, protocol=pickle.HIGHEST_PROTOCOL)

    population = newPopulation(last_population=population)
