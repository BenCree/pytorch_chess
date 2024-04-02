import pandas as pd
import torch
import chess
import chess.pgn
import numpy as np
import re
from board_state import state
import torch


test_fen = '4k2r/6r1/8/8/8/8/3R4/R3K3 w Qk - 0 1'

state.parse_fen(fen=test_fen)


def read_data(data, game_num=5):
    res_dict = {'1-0': 1, '0-1': 0, '1/2-1/2': 0.5}
    curr_game = 0
    games = []
    y = []
    for dset in data:
        pgn = open(dset)
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            curr_game += 1

            res = game.headers['Result']
            res_array = np.array(res_dict[res])
            board = game.board()
            length = game.headers['PlyCount']
            #print(f'game length: {length}')

            states = []
            for move in game.mainline_moves():
                #print(f'fen {board.fen()}')
                board_state = state(board)
                board_array = board_state.to_array()



                states.append(board_array)

                board.push(move)

            assert int(game.headers['PlyCount']) == len(states)
            states = torch.Tensor(states)
            #print(len(states), states)
            games.append(states)
            y.append(res_array)
            print(f'parsed game {curr_game}, {len(states)} moves')
            if curr_game > game_num:
                break
        print(games)

        y = np.array(y)
        y = torch.tensor(y)
        return games, y



if __name__ == '__main__':
    data = ['ficsgamesdb_2023_standard2000_nomovetimes_330240.pgn']
    games, res = read_data(data, 1000)
    print(games[0], res[0])

#
# while True:
#
#
#     game = chess.pgn.read_game(pgn)
#     #print(game.headers)
#     res = game.headers['Result']
#
#     if res is None or game_num > 5:
#         break
#     else:
#         print(res)
#         board = game.board()
#         length = game.headers['PlyCount']
#         print(f'game length: {length}')
#         game_num += 1
#         states = []
#         for move in game.mainline_moves():
#             #print(f'fen {board.fen()}')
#             board_state = state(board)
#             board_array = board_state.to_array()
#
#             states.append([board_array, res_dict[res]])
#             #print(array)
#             board.push(move)
#         #print(states)
#         assert int(game.headers['PlyCount']) == len(states)
#         dat.append(states)
# #
#print(f'training dat: {dat}')
#
# for game in dat[-1]:
#     print(len(game))
    # for move in game:
    #  print(move)







