#-*- coding: utf8 -*-
from django import http
from django.views.generic.base import TemplateView, View
from interview import models

import json
import yaml
from django.core.urlresolvers import reverse, resolve
input = open('interview/input.txt')
input = yaml.load(input.read())
models_list = input.keys()


class MainView(TemplateView):
    template_name = 'main.html'
    
    def get_context_data(self):
        context = super(MainView, self).get_context_data()
        models = []
        for model in models_list:
            models.append([model, reverse('ajax', kwargs={'model_name': model})])
        context['models'] = models
        return context


class JSONResponseView(View):
    def get(self, request, model_name):
        if hasattr(models, model_name):
            model = getattr(models, model_name)
            data = model.objects.all().order_by('id')
            return self.render_to_response({'data': data})
        else:
            return False
            
    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        objects = context['data']
        data = {'0': [field.name for field in objects[0]._meta.fields]}
        for object in objects:
            row = []
            for field in object._meta.fields:
                row.append(getattr(object, field.name))
            data[object.pk] = row
            
        return json.dumps(data)
     
     
     
     
     
     