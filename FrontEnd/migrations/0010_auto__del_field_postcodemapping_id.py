# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PostcodeMapping.id'
        db.delete_column(u'FrontEnd_postcodemapping', 'id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'PostcodeMapping.id'
        raise RuntimeError("Cannot reverse this migration. 'PostcodeMapping.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'PostcodeMapping.id'
        db.add_column(u'FrontEnd_postcodemapping', 'id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


    models = {
        u'FrontEnd.addressrecord': {
            'Meta': {'ordering': "('postcode', 'address_1')", 'object_name': 'AddressRecord'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'council_ref': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'council_tax_band': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_authority': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'main_door': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'postcode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['FrontEnd.PostcodeMapping']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'FrontEnd.geographicalboundary': {
            'Meta': {'object_name': 'GeographicalBoundary'},
            'boundary_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'FrontEnd.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['FrontEnd.AddressRecord']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'FrontEnd.postcodemapping': {
            'Meta': {'object_name': 'PostcodeMapping'},
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'FrontEnd.region': {
            'Meta': {'object_name': 'Region'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'area_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'descript0': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'descript1': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'descriptio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'hectares': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'number': ('django.db.models.fields.FloatField', [], {}),
            'number0': ('django.db.models.fields.FloatField', [], {}),
            'polygon_id': ('django.db.models.fields.FloatField', [], {}),
            'type_cod0': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'type_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'unit_id': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['FrontEnd']