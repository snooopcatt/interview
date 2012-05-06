# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Test'
        db.create_table('interview_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('interview', ['Test'])

        # Adding model 'users'
        db.create_table('interview_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('paycheck', self.gf('django.db.models.fields.IntegerField')()),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('interview', ['users'])

        # Adding model 'rooms'
        db.create_table('interview_rooms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('spots', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('interview', ['rooms'])

    def backwards(self, orm):
        # Deleting model 'Test'
        db.delete_table('interview_test')

        # Deleting model 'users'
        db.delete_table('interview_users')

        # Deleting model 'rooms'
        db.delete_table('interview_rooms')

    models = {
        'interview.rooms': {
            'Meta': {'object_name': 'rooms'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {})
        },
        'interview.test': {
            'Meta': {'object_name': 'Test'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test': ('django.db.models.fields.IntegerField', [], {})
        },
        'interview.users': {
            'Meta': {'object_name': 'users'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['interview']