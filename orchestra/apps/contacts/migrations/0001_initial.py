# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('national_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='Barcelona', max_length=128, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(default='Barcelona', max_length=20, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Spain', max_length=20)),
            ('type', self.gf('django.db.models.fields.CharField')(default='INDIVIDUAL', max_length=32)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=256, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('register_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding model 'Contract'
        db.create_table(u'contacts_contract', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('register_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('cancel_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Contract'])

        # Adding unique constraint on 'Contract', fields ['content_type', 'object_id']
        db.create_unique(u'contacts_contract', ['content_type_id', 'object_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Contract', fields ['content_type', 'object_id']
        db.delete_unique(u'contacts_contract', ['content_type_id', 'object_id'])

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Deleting model 'Contract'
        db.delete_table(u'contacts_contract')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "'Barcelona'", 'max_length': '128', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Spain'", 'max_length': '20'}),
            'full_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'national_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'Barcelona'", 'max_length': '20', 'blank': 'True'}),
            'register_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'INDIVIDUAL'", 'max_length': '32'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'contacts.contract': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'Contract'},
            'cancel_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'register_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contacts']