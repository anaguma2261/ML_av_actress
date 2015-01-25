#! /usr/bin/python
# -*- encoding: utf-8 -*-

from sample_extract_feature import *
import unittest
from os import path
APP_ROOT = path.dirname( path.abspath( __file__ ) ) + "../"

class TestSampleExtractFeature(unittest.TestCase):

    def setUp(self):
        self.folder_path = "test_image/"
        self.target = SampleExtractFeature(self.folder_path)


    def test_extract_surf_features(self):
        img_ids = ["11", "13", "17", "23", "25", "27", "3", "32", "33", "4", "43",
                    "46", "6", "60", "61", "63", "79", "8", "80", "88", "89"]
        for img_id in self.target._extract_surf_features_for_all_images().keys():
            self.assertTrue(img_id in img_ids)

        self.target.to_csv("test.csv")


    def test_get_nearest_actress(self):
        nearest_actresses = self.target.get_nearest_actresses(path.join(self.folder_path, "11.jpg"))
        assert len(nearest_actresses) == 3
        assert nearest_actresses[0] == "11"

    def test_get_nearest_actress_with_limit(self):
        nearest_actresses = self.target.get_nearest_actresses(path.join(self.folder_path, "11.jpg"), limit=5)
        assert len(nearest_actresses) == 5
        assert nearest_actresses[0] == "11"
