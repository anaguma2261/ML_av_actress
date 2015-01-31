# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from lib.similarity.anaguma2261 import Similarity
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import csv
import os


_BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def show(request, img_id):
    sm = Similarity()
    sim_ids = sm.get_similar_actresses(
        _BASE_PATH + '/../static/images/%s.jpg'%img_id
    )

    return render_to_response('show.html',
                          {"sim_ids":sim_ids, "img_id":img_id},
                          context_instance=RequestContext(request))

def upload(request):
    if request.method == "POST":

        file = request.FILES['target_image']
        path = default_storage.save('static/tmp/i', ContentFile(file.read()))

        sm = Similarity()
        sim_ids = sm.get_similar_actresses(path)

        av_profiles_path = os.path.normpath(os.path.join(_BASE_PATH, '../../data/profile.csv'))
        with open(av_profiles_path, 'r') as f:
            reader = csv.reader(f)
            prof_dict = { str(row[0]):[row[1].decode('shift-jis'),\
                                       row[2].decode('shift-jis'),\
                                       row[3].decode('shift-jis'),\
                                       row[4].decode('shift-jis'),\
                                       row[5].decode('shift-jis'),\
                                       row[6].decode('shift-jis'),\
                                       row[7].decode('shift-jis')\
                                       ] for row in reader\
                          if str(row[0]) in map(str, sim_ids) }

        return render_to_response('show.html',
                              {"prof_dict":prof_dict, "upload":'/'+path},
                              context_instance=RequestContext(request))

    return render_to_response('upload.html',
                              context_instance=RequestContext(request))
