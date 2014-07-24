# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Changing field 'Region.geom'
        db.alter_column(u'FrontEnd_region', 'geom',
                        self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=27700))

    def backwards(self, orm):
        # Changing field 'Region.geom'
        db.alter_column(u'FrontEnd_region', 'geom',
                        self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=-1))

    models = {
        u'FrontEnd.address': {
            'Meta': {'ordering': "('postcode', 'address_1')", 'object_name': 'Address'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['FrontEnd.Address']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'FrontEnd.postcodemapping': {
            'Meta': {'object_name': 'PostcodeMapping'},
            'id': ('django.db.models.fields.IntegerField', [], {}),
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
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '27700'}),
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