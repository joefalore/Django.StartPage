# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contact.message'
        db.alter_column(u'contact_contact', 'message', self.gf('django.db.models.fields.TextField')(max_length=3000))

    def backwards(self, orm):

        # Changing field 'Contact.message'
        db.alter_column(u'contact_contact', 'message', self.gf('django.db.models.fields.CharField')(max_length=3000))

    models = {
        u'contact.contact': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '220'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contact']