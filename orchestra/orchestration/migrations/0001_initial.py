# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Server'
        db.create_table(u'orchestration_server', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('os', self.gf('django.db.models.fields.CharField')(default='LINUX', max_length=32)),
        ))
        db.send_create_signal(u'orchestration', ['Server'])

        # Adding model 'ScriptLog'
        db.create_table(u'orchestration_scriptlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='RECEIVED', max_length=16)),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(related_name='execution_logs', to=orm['orchestration.Server'])),
            ('script', self.gf('django.db.models.fields.TextField')()),
            ('stdout', self.gf('django.db.models.fields.TextField')()),
            ('stderr', self.gf('django.db.models.fields.TextField')()),
            ('traceback', self.gf('django.db.models.fields.TextField')()),
            ('exit_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('task_id', self.gf('django.db.models.fields.CharField')(max_length=36, unique=True, null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'orchestration', ['ScriptLog'])


    def backwards(self, orm):
        # Deleting model 'Server'
        db.delete_table(u'orchestration_server')

        # Deleting model 'ScriptLog'
        db.delete_table(u'orchestration_scriptlog')


    models = {
        u'orchestration.scriptlog': {
            'Meta': {'object_name': 'ScriptLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exit_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'script': ('django.db.models.fields.TextField', [], {}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'execution_logs'", 'to': u"orm['orchestration.Server']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'RECEIVED'", 'max_length': '16'}),
            'stderr': ('django.db.models.fields.TextField', [], {}),
            'stdout': ('django.db.models.fields.TextField', [], {}),
            'task_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'unique': 'True', 'null': 'True'}),
            'traceback': ('django.db.models.fields.TextField', [], {})
        },
        u'orchestration.server': {
            'Meta': {'object_name': 'Server'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'os': ('django.db.models.fields.CharField', [], {'default': "'LINUX'", 'max_length': '32'})
        }
    }

    complete_apps = ['orchestration']