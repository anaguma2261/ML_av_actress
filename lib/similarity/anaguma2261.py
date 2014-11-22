# -*- coding: utf-8 -*-

from lib.similarity.base import Base
import cv
import os
import cPickle as pickle
KMEANS_OBJECT_PATH = os.path.normpath(os.path.join(_BASE_PATH, '../../data/kmeans.pkl'))

class Similarity(Base):

    def __init__(self):
        Base.__init__(self)
        with open(KMEANS_OBJECT_PATH) as f:
            self.kmeans = pickle.load(f)


    def get_similar_actresses(self, target_image_path):

        img = cv.LoadImageM(img_path , cv.CV_LOAD_IMAGE_GRAYSCALE)

        (keypoints, descriptors) = cv.ExtractSURF(img, None,
                                                       cv.CreateMemStorage(),
                                                       (1 , 500, 3, 4))


        return [8070, 236, 14996, 18367, 10228]

if __name__ == '__main__':
    s = Similarity()
    print s.get_similar_actresses('')

