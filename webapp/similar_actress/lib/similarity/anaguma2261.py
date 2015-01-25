# -*- coding: utf-8 -*-

from base import Base
import pandas
import numpy
import cv
import os
import cPickle as pickle
import os

class Similarity(Base):
    AV_FEATURES_INDEX_COLUMN = "img_id"

    _BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    KMEANS_OBJECT_PATH = os.path.normpath(os.path.join(_BASE_PATH,
                                      '../../../../data/kmeans.pkl'))


    def __init__(self):
        Base.__init__(self)
        with open(self.KMEANS_OBJECT_PATH) as f:
            self.kmeans = pickle.load(f)

        self.pd_feature_data = pandas.read_csv(self.AV_FEATURES_PATH,
                                            index_col=self.AV_FEATURES_INDEX_COLUMN)

    def get_similar_actresses(self, target_image_path):

        img = cv.LoadImageM(target_image_path , cv.CV_LOAD_IMAGE_GRAYSCALE)

        (keypoints, descriptors) = cv.ExtractSURF(img, None,
                                                       cv.CreateMemStorage(),
                                                       (1 , 500, 3, 4))

        bag_of_keypoints = self._calc_a_bag_of_keypoints(descriptors)


        #distance = ((self.pd_feature_data - bag_of_keypoints)**2).sum(axis=1)
        distance = ((self.pd_feature_data * bag_of_keypoints)).sum(axis=1)
        distance.sort(ascending=False)
        return distance.index.values[0]

    def _calc_a_bag_of_keypoints(self, descriptors):
        bag_of_keypoints = numpy.zeros(self.kmeans.cluster_centers_.shape[0])

        for nearest_centroid in self.kmeans.predict(descriptors):
            bag_of_keypoints[nearest_centroid] += 1

        bag_of_keypoints /= len(descriptors)

        return bag_of_keypoints




if __name__ == '__main__':
    s = Similarity()
    img_id = s.get_similar_actresses('../../sample/3996.jpg')

    assert img_id == 2132
