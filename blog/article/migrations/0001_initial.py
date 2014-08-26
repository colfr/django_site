# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorie'
        db.create_table(u'article_categorie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'article', ['Categorie'])

        # Adding model 'article'
        db.create_table(u'article_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['article.Categorie'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'article', ['article'])


    def backwards(self, orm):
        # Deleting model 'Categorie'
        db.delete_table(u'article_categorie')

        # Deleting model 'article'
        db.delete_table(u'article_article')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'article'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Categorie']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'article.categorie': {
            'Meta': {'object_name': 'Categorie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['article']