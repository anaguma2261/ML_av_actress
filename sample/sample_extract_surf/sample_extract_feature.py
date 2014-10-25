# -*- encoding: utf-8 -*-

import cv
import numpy
import glob
from os import path
import re
from sklearn.cluster import MiniBatchKMeans
from logging import getLogger

class SampleExtractFeature(object):
    '''
    サンプルの画像からの特徴抽出
    :param folder_path str: 画像の入ってるフォルダパス
    :param cluster_num int: 画像特徴の次元数
    '''

    IMG_ID_REGREX = re.compile(r'(\d+)\.(jpg)|(JPG)|(jpeg)|(JPEG)$')
    KMEANS_ITER_NUM = 100
    logger = getLogger(__name__)

    def __init__(self, folder_path, cluster_num=100):

        self.folder_path = folder_path
        self.cluster_num = cluster_num

        map_surf_features = self._extract_surf_features()
        self.kmeans       = self._calc_kmeans_centroid(map_surf_features)
        self.bags_of_keypoints = { img_id: self._calc_a_bag_of_keypoints(descriptors)
                                            for img_id, descriptors
                                             in map_surf_features.items() }

    def _extract_surf_features(self):
        self.logger.debug("enter")
        images = glob.glob(self.folder_path + '*.jpg')

        if len(images) == 0:
            raise Exception("%s has no image file."%sself.folder_path)

        map_surf_features = {}
        for img_path in images:
            image_id = self.IMG_ID_REGREX.search(img_path).group(1)
            img = cv.LoadImageM(img_path , cv.CV_LOAD_IMAGE_GRAYSCALE)

            #: ハードコーディングすみません 意味をその内調べます。
            (keypoints, descriptors) = cv.ExtractSURF(img, None,
                                                       cv.CreateMemStorage(),
                                                       (1 , 500, 3, 4))
            map_surf_features[image_id] = descriptors
        self.logger.debug("exit")

        return map_surf_features

    def _calc_kmeans_centroid(self, map_surf_features):
        self.logger.debug("enter")

        image_data = []
        for surf_feature in map_surf_features.values():
            image_data += surf_feature
        image_data = numpy.array(image_data)
        #print image_data
        """
        centroid, label = kmeans2(image_data,
                                  k=self.cluster_num,
                                  minit="points",
                                  iter=KMEANS_ITER_NUM)
        """
        kmeans = MiniBatchKMeans(n_clusters=self.cluster_num,
                                 max_iter=self.KMEANS_ITER_NUM)

        label = kmeans.fit_predict(image_data)
        centroid = kmeans.cluster_centers_
        self.logger.debug("exit")

        return kmeans

    def _calc_a_bag_of_keypoints(self, descriptors):
        bag_of_keypoints = numpy.zeros(self.cluster_num)

        for nearest_centroid in self.kmeans.predict(descriptors):
            bag_of_keypoints[nearest_centroid] += 1

        bag_of_keypoints /= len(descriptors)
        return bag_of_keypoints

    def to_csv(self, csv_path):
        self.logger.debug("enter")

        with open(csv_path, "w") as f:
            f.write("img_id,")
            f.write(",".join(["feature_%s"%i for i in xrange(self.cluster_num)]))
            f.write("\n")

            for img_id, bag_of_keypoints in self.bags_of_keypoints.items():
                f.write(str(img_id)+",")
                f.write(",".join(map(str, bag_of_keypoints)))
                f.write("\n")

        self.logger.debug("exit")
