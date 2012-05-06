#-*- coding: utf8 -*-
import yaml
from django.db.models import Model
from django.db.models.fields import CharField, IntegerField
import copy
    
input = open('interview/input.txt')
input = yaml.load(input.read())

# у charfields требует max_length, поэтому заворачиваем конструктор в функцию
def create_charfield(max_len=255, **kwargs):
    return CharField(max_length=max_len, **kwargs)

types = {'char': create_charfield, 'int': IntegerField}

for model_name, descr in input.iteritems():
    # джанго требует это в качестве app_label
    fields = {'__module__': 'interview.models',}
    
    # создаем словарь, содержащий имена полей и инстанцированные объекты
    for field in descr['fields']:
        fields.update({ field['id']: types[field['type']](verbose_name=field['title'])})
        
    # создаем класс модели        
    new_model = type(model_name, (Model,), fields)
    
    # кладем ее в глобальную область видимости
    globals()[model_name] = new_model
