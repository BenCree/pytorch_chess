import pandas as pd
import torch
import chess
import chess.pgn
import numpy as np
import re
from board_state import state
pgn = open('ficsgamesdb_2023_standard2000_nomovetimes_330240.pgn')


game_num = 0
dat = []
res_dict = {'1-0':1,'0-1':0,'1/2-1/2':0.5}
test_fen = '4k2r/6r1/8/8/8/8/3R4/R3K3 w Qk - 0 1'

state.parse_fen(fen=test_fen)
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
#
#print(f'training dat: {dat}')

for game in dat[-1]:
    print(len(game))
    for move in game:
     print(move)





