# -*- encoding: utf-8 -*-

import os
import librosa


class data_io:

    @staticmethod
    def get_list(_dir):  # 获取_dataset中csv文件目录

        _list = []

        for dir_path, dirname, filenames in os.walk(_dir):
            for filename in filenames:
                if '.wav' in os.path.split(filename)[-1] or '.mp3' in os.path.split(filename)[-1] or '.mfcc' in os.path.split(filename)[-1]:
                    _list.append(os.path.join(filename))

        return _list

    @staticmethod
    def get_mfcc(n):

        y, sr = librosa.load('./_sounds/' + n, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

        return mfcc
