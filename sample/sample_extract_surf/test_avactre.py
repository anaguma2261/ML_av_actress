#! /usr/bin/python
# -*- encoding: utf-8 -*-

from sample_extract_feature import *
import unittest
from os import path
APP_ROOT = path.dirname( path.abspath( __file__ ) ) + "../"

class TestSampleExtractFeature(unittest.TestCase):

    def setUP(self):
        pass


    def test_extract_surf_features(self):

        folder_path = "test_image/"
        sef = SampleExtractFeature(folder_path)

        img_ids = ["11", "13", "17", "23", "25", "27", "3", "32", "33", "4", "43",
                    "46", "6", "60", "61", "63", "79", "8", "80", "88", "89"]
        for img_id in  sef._extract_surf_features().keys():
            self.assertTrue(img_id in img_ids)

        sef.to_csv("test.csv")
