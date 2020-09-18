import sys
import chess
sys.path.append(".")

import settings
from neural_network import *
from genetic_algorithm.fitness_function import *

class Individual():

    def __init__(self):
        self.neural_network = NeuralNetwork()
        self.fitness = 0
        self.minmax_depth = settings.minmax['depth']

    def getInputLayer(self, board):
    
        turn = board.turn
        board = str(board)
        
        board = board.replace('\n', ' ').split(' ')

        input_layer = []

        for piece in board:
            
            layer = [0,0,0,0,0,0,0,0,0,0,0,0]

            if piece == 'r':
                layer[0] = 1
            if piece == 'n':
                layer[1] = 1
            if piece == 'b':
                layer[2] = 1
            if piece == 'q':
                layer[3] = 1
            if piece == 'k':
                layer[4] = 1
            if piece == 'p':
                layer[5] = 1

            if piece == 'R':
                layer[6] = 1
            if piece == 'N':
                layer[7] = 1
            if piece == 'B':
                layer[8] = 1
            if piece == 'Q':
                layer[9] = 1
            if piece == 'K':
                layer[10] = 1
            if piece == 'P':
                layer[11] = 1

            if turn:
                aux = layer[:6].copy()
                layer[:6] = layer [6:].copy()
                layer[6:] = aux.copy()

            for i in layer:
                input_layer.append(i)

        return input_layer

    def getScore(self, board):

        input_layer = self.getInputLayer(board)
        score = self.neural_network.feedFoward(input_layer)[0]

        return score

    def minimax(self, is_max_turn, board, depth):

        scores = []
        for move in board.legal_moves:
            
            board.push(move)

            if depth == 0:
                scores.append(self.minimax(not is_max_turn, board, depth-1))
            else:
                scores.append(self.getScore(board))
            
            board.pop()

        return max(scores) if is_max_turn else min(scores)

    def playTurn(self, board):

        best_score = None

        for move in board.legal_moves:
    
            board.push(move)

            score = self.minimax(False, board, self.minmax_depth)
            
            if best_score == None:
                best_score = score
                best_move = move

            if (score > best_score):
                best_score = score
                best_move = move
 
            board.pop()

        board.push(best_move)

    def viewFitness(self):
        return self.fitness
