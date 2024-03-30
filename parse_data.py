import pandas as pd
import torch
import chess
import chess.pgn
import numpy as np
import re
pgn = open('ficsgamesdb_2023_standard2000_nomovetimes_330240.pgn')

class state():
    '''wrapper around chess.board'''
    def __init__(self, board):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board
        #print(board)

    def parse_fen(self, fen):
        self.fen = fen
        return fen
    def to_array(self):
        '''64 bit array '''
        # piece_dict = {'R': 1, 'N': 2, 'B': 3, 'K': 4, 'Q': 5, \
        #               'r': 6, 'n': 7, 'b': 8, 'k': 9, 'q': 10}
        state_array = np.zeros(64, np.uint16)
        fen = board.fen()
        for i in range(64):
            if board.piece_at(i) is not None:
                state_array[i] = board.piece_at(i).piece_type
            else:
                state_array[i] = 0
        #print(state_array)
        return state_array
        # TODO: add flags for castling, en passant, and anything else that isnt a basic board position

game_num = 0
dat = []
res_dict = {'1-0':1,'0-1':0,'1/2-1/2':0.5}
while True:


    game = chess.pgn.read_game(pgn)
    #print(game.headers)
    res = game.headers['Result']

    if res is None or game_num > 5:
        break
    else:
        print(res)
        board = game.board()
        length = game.headers['PlyCount']
        print(f'game length: {length}')
        game_num += 1
        states = []
        for move in game.mainline_moves():
            #print(f'fen {board.fen()}')
            board_state = state(board)
            board_array = board_state.to_array()
            states.append([board_array, res_dict[res]])
            #print(array)
            board.push(move)
        #print(states)
        assert int(game.headers['PlyCount']) == len(states)
        dat.append(states)

print(f'training dat: {dat}')
for d in dat:
    print(len(d))




