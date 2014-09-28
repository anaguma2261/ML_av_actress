#! /usr/bin/python
# -*- encoding: utf-8 -*-
import cv
import numpy
import glob
from os import path
import re
from scipy.cluster.vq import vq, kmeans, kmeans2, whiten

IMG_ID_REGREX = re.compile(r'(\d+)\.(jpg)|(JPG)|(jpeg)|(JPEG)$')
KMEANS_ITER_NUM = 100

class SampleExtractFeature(object):
    '''
    サンプルの画像からの特徴抽出
    :param folder_path str: 画像の入ってるフォルダパス
    :param cluster_num int: 画像特徴の次元数
    '''


    def __init__(self,
                 folder_path,
                 cluster_num=100):


        self.folder_path = folder_path
        self.cluster_num = cluster_num

        self.map_surf_features = self._extract_surf_features()
        self.centroid, self.label = self._calc_kmeans_centroid()
        self.map_bag_of_keypoints = self._calc_bag_of_keypoints()

    def _extract_surf_features(self):

        images = glob.glob(self.folder_path + '*.jpg')
        map_surf_features = {}
        for img_path in images:
            image_id = IMG_ID_REGREX.search(img_path).group(1)
            img = cv.LoadImageM(img_path , cv.CV_LOAD_IMAGE_GRAYSCALE)

            #: ハードコーディングすみません 意味をその内調べます。
            (keypoints, descriptors) = cv.ExtractSURF(img, None,
                                                       cv.CreateMemStorage(),
                                                       (1 , 500, 3, 4))
            map_surf_features[image_id] = descriptors

        return map_surf_features

    def _calc_kmeans_centroid(self):

        image_data = []
        for surf_feature in self.map_surf_features.values():
            image_data += surf_feature
        image_data = numpy.array(image_data)
        #print image_data
        centroid, label = kmeans2(image_data,
                                  k=self.cluster_num,
                                  minit="points",
                                  iter=KMEANS_ITER_NUM)
        return centroid, label

    def _calc_bag_of_keypoints(self):

        map_bag_of_keypoints = {}
        for img_id, descriptors in self.map_surf_features.items():

            bag_of_keypoints = numpy.zeros(self.cluster_num)
            for descriptor in descriptors:
                centroid_distances = [numpy.linalg.norm(self.centroid[i] - descriptor)
                                      for i in xrange(self.cluster_num)]

                nearest_centroid = numpy.argsort(centroid_distances)[0]
                bag_of_keypoints[nearest_centroid] += 1

            bag_of_keypoints /= len(descriptors)
            map_bag_of_keypoints[img_id] = bag_of_keypoints

        return map_bag_of_keypoints

    def to_csv(self, csv_path):

        with open(csv_path, "w") as f:
            f.write("img_id,")
            f.write(",".join(["feature_%s"%i for i in xrange(self.cluster_num)]))
            f.write("\n")

            for img_id, bag_of_keypoints in self.map_bag_of_keypoints.items():
                f.write(str(img_id)+",")
                f.write(",".join(map(str, bag_of_keypoints)))
                f.write("\n")


