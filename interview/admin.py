#-*- coding: utf8 -*-
from django.contrib import admin
import yaml
input = open('interview/input.txt')
input = yaml.load(input.read())

# импортируем все, чтобы не возиться с именами
from interview import models

for model_name, descr in input.iteritems():
    # just for fun получим список полей. а почему бы и нет, правильно?
    fields = []
    for field in descr['fields']:
        fields.append(field['id'])
    new_admin_class = type('{0}Admin'.format(model_name), (admin.ModelAdmin,), {'fields': fields})
    a = model_name
    admin.site.register(getattr(models, model_name), new_admin_class)
    