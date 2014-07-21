# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'GeographicalBoundary'
        db.create_table(u'FrontEnd_geographicalboundary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('boundary_type', self.gf('django.db.models.fields.IntegerField')()),
            ('mpoly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'FrontEnd', ['GeographicalBoundary'])


    def backwards(self, orm):
        # Deleting model 'GeographicalBoundary'
        db.delete_table(u'FrontEnd_geographicalboundary')


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
        }
    }

    complete_apps = ['FrontEnd']