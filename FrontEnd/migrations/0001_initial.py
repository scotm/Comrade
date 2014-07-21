# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'PostcodeMapping'
        db.create_table(u'FrontEnd_postcodemapping', (
            ('id', self.gf('django.db.models.fields.IntegerField')()),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'FrontEnd', ['PostcodeMapping'])

        # Adding model 'Address'
        db.create_table(u'FrontEnd_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address_3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('postcode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['FrontEnd.PostcodeMapping'])),
        ))
        db.send_create_signal(u'FrontEnd', ['Address'])

        # Adding model 'Person'
        db.create_table(u'FrontEnd_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['FrontEnd.Address'])),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
        ))
        db.send_create_signal(u'FrontEnd', ['Person'])


    def backwards(self, orm):
        # Deleting model 'PostcodeMapping'
        db.delete_table(u'FrontEnd_postcodemapping')

        # Deleting model 'Address'
        db.delete_table(u'FrontEnd_address')

        # Deleting model 'Person'
        db.delete_table(u'FrontEnd_person')


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