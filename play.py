import pickle
import chess

from genetic_algorithm.populations import *

population = newPopulation(random_start=True)

game = chess.Board()
population.actual_individual = 0

population.individuals[0].doAction(game)