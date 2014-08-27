# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.text_markup_type'
        db.add_column(u'article_article', 'text_markup_type',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=30),
                      keep_default=False)

        # Adding field 'Article._text_rendered'
        db.add_column(u'article_article', '_text_rendered',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Article.text'
        db.alter_column(u'article_article', 'text', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

    def backwards(self, orm):
        # Deleting field 'Article.text_markup_type'
        db.delete_column(u'article_article', 'text_markup_type')

        # Deleting field 'Article._text_rendered'
        db.delete_column(u'article_article', '_text_rendered')


        # Changing field 'Article.text'
        db.alter_column(u'article_article', 'text', self.gf('django.db.models.fields.TextField')())

    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Categorie']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'text_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'article.categorie': {
            'Meta': {'object_name': 'Categorie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['article']