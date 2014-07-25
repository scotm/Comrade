# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'FrontEnd_address')

        # Adding model 'AddressRecord'
        db.create_table(u'FrontEnd_addressrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address_3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('local_authority', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('postcode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['FrontEnd.PostcodeMapping'])),
            ('council_ref', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('council_tax_band', self.gf('django.db.models.fields.CharField')(default='A', max_length=5)),
        ))
        db.send_create_signal(u'FrontEnd', ['AddressRecord'])


        # Changing field 'Person.address'
        db.alter_column(u'FrontEnd_person', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['FrontEnd.AddressRecord']))

    def backwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'FrontEnd_address', (
            ('postcode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['FrontEnd.PostcodeMapping'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('council_tax_band', self.gf('django.db.models.fields.CharField')(default='A', max_length=5)),
            ('local_authority', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address_3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('council_ref', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal(u'FrontEnd', ['Address'])

        # Deleting model 'AddressRecord'
        db.delete_table(u'FrontEnd_addressrecord')


        # Changing field 'Person.address'
        db.alter_column(u'FrontEnd_person', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['FrontEnd.Address']))

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