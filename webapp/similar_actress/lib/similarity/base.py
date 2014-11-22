# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os

class Base(object):

    __metaclass__ = ABCMeta

    _BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    AV_PROFILES_PATH = os.path.normpath(os.path.join(_BASE_PATH, '../../../../data/profile.csv'))
    AV_FEATURES_PATH = os.path.normpath(os.path.join(_BASE_PATH, '../../../../data/av_actress_features.csv'))

    def __init__(self):
        pass

    @abstractmethod
    def get_similar_actresses(self, target_image_path): pass
