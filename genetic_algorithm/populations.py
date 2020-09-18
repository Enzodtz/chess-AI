import sys
import chess
sys.path.append(".")

from genetic_algorithm.individuals import *
from genetic_algorithm.random_start import *
from genetic_algorithm.parent_selection import *
from genetic_algorithm.parent_crossover import *
from genetic_algorithm.mutations import *
from logger import *
import settings

class Population():
    
    def __init__(self):
        
        self.size = settings.population['population size']
        if self.size % 2 != 0:
            raise Exception('Population size needs to be odd!')
        
        self.individuals = []
        for _ in range(self.size):
            self.individuals.append(Individual())

        self.games_number = int(self.size/2)

    def playGames(self, generation="-"):
    
        printGeneration(generation)

        for i in range(0, self.games_number, 2):

            printGameNumber(i, self.games_number)

            player_1 = self.individuals[i]
            player_2 = self.individuals[i + 1]

            board = chess.Board()

            while not board.is_game_over():
                printBoard(board)    
                player_1.playTurn(board)
                printBoard(board)         
                player_2.playTurn(board)

            printBoard(board)

            if board.result() == '1-0':
                player_1.fitness = 2
                player_2.fintess = 0

            elif board.result() == '1/2-1/2':
                player_1.fitness = 1
                player_2.fitness = 1
            
            else:
                player_1.fitness = 0
                player_2.fitness = 2

def newPopulation(random_start=False, last_population=None):

    population = Population()

    if random_start:

        population = randomStart(population)

    else:

        parents = parentSelection(last_population)
        population = parentCrossover(population, parents)
        population = mutate(population)

    return population