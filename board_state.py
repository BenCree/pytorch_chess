import pandas as pd
import torch
import chess
import chess.pgn
import numpy as np
import re


class state():
    '''wrapper around chess.board'''
    def __init__(self, board):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board
        #print(board)
    def get_fen(self):
        fen = board.fen()
        return fen
    @staticmethod
    def parse_fen(fen):
        fen = fen.split(' ')
        castling_array = np.zeros(4, np.uint16)
        enpassant_array = np.zeros(1, np.uint16)
        castle_fen = fen[2]
        enpassant_sq = fen[3]
        castling_key = {'K': 0, 'Q': 1, 'k': 2, 'q': 3}

        for state in castle_fen:
            if state in castling_key:
                castling_array[castling_key[state]] = 1
        if enpassant_sq != '-':
            enpassant_array[0] = 1
        fen_array = np.concatenate((castling_array, enpassant_array), axis=0)
        # print(f'castling state {castle_fen}')
        # print(f'castling array {castling_array}')
        # print(f'fen array {fen_array}')
        return fen_array
    def to_array(self):
        '''64 bit array '''
        # piece_dict = {'R': 1, 'N': 2, 'B': 3, 'K': 4, 'Q': 5, \
        #               'r': 6, 'n': 7, 'b': 8, 'k': 9, 'q': 10}
        board = self.board
        state_array = np.zeros(64, np.uint16)
        fen = board.fen()
        fen = fen.split(' ')
        for i in range(64):
            if board.piece_at(i) is not None:
                state_array[i] = board.piece_at(i).piece_type
            else:
                state_array[i] = 0
        #print(state_array)
        castling_array = np.zeros(4, np.uint16)
        enpassant_array = np.zeros(1, np.uint16)
        castle_fen = fen[2]
        enpassant_sq = fen[3]
        castling_key = {'K': 0, 'Q': 1, 'k': 2, 'q': 3}

        for state in castle_fen:
            if state in castling_key:
                castling_array[castling_key[state]] = 1
        if enpassant_sq != '-':
            enpassant_array[0] = 1
        cstl_npsnt_array = np.concatenate((castling_array, enpassant_array), axis=0)
        full_array = np.concatenate((state_array, cstl_npsnt_array), axis=0)
        # print(f'castling state {castle_fen}')
        # print(f'castling array {castling_array}')
        # print(f'fen array {fen_array}')
        return full_array
