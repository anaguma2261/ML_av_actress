# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from lib.similarity.anaguma2261 import Similarity
import os

_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
def show(request, img_id):

    sm = Similarity()
    sim_id = sm.get_similar_actresses(_BASE_PATH + '/../static/images/%s.jpg'%img_id)

    map_dic = {"sim_id":sim_id, "img_id":img_id}

    return render_to_response('show.html',
                              {"sim_id":sim_id, "img_id":img_id},
                              context_instance=RequestContext(request))
