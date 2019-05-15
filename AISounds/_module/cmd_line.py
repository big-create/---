# -*- encoding: utf-8 -*-

import sys

import numpy as np

from .data_io import data_io

_dir = sys.path[0]


class cmd_Line:

    def __init__(self, path):
        self.path = path
        self.L = self.building()

    def building(self):
        print("Building list...")
        _list = data_io.get_list(self.path)
        print("List is built.\nData will be loaded from list.")

        return _list

    def pre_process(self):

        print('Start generate the mfcc files...')
        for n in self.L:
            mfcc = data_io.get_mfcc(n)  # 40维的矩阵
            np.save('./_mfcc/' + n + '.npy', mfcc)
            print('The %s is generated.' % n)
