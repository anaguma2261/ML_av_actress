# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from lib.similarity.anaguma2261 import Similarity
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


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

        return render_to_response('show.html',
                              {"sim_ids":sim_ids, "upload":'/'+path},
                              context_instance=RequestContext(request))

    return render_to_response('upload.html',
                              context_instance=RequestContext(request))
