# -*- coding: utf-8 -*-

from lib.similarity.base import Base

class Similarity(Base):

    def __init__(self):
        Base.__init__(self)

    def get_similar_actresses(self, target_image_path):
        return [8070, 236, 14996, 18367, 10228]

if __name__ == '__main__':
    s = Similarity()
    print s.get_similar_actresses('')
