import csv

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


def process_postcode_data(line):
    return PostcodeMapping(id=line['id'], postcode=line['postcode'],
                           point=Point(float(line['longitude']), float(line['latitude'])))


def postcode_chunks(reader, length):
    postcodes = []
    for i, line in enumerate(reader, start=1):
        postcodes.append(process_postcode_data(line))
        if len(postcodes) == length:
            yield postcodes
            postcodes = []
    yield postcodes


class PostcodeMapping(models.Model):
    id = models.IntegerField()
    postcode = models.CharField(max_length=10, primary_key=True)
    # GeoDjango-specific declarations
    point = models.PointField()
    objects = models.GeoManager()

    def get_addresses(self):
        return Address.objects.filter(postcode=self)

    def __unicode__(self):
        return self.postcode

    @staticmethod
    def match_postcode(postcode):
        return PostcodeMapping.objects.get(postcode=postcode.replace(' ', ''))

    @staticmethod
    def fill_up_db(postcode_filename):
        import time

        start_time = time.time()
        chunk_size = 200000
        i = 0
        with open(postcode_filename) as myfile:
            reader = csv.DictReader(myfile)
            for chunk in postcode_chunks(reader, chunk_size):
                PostcodeMapping.objects.bulk_create(chunk)
                i += chunk_size
                print "%d records written over %f" % (i, time.time() - start_time)


class Address(models.Model):
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    postcode = models.ForeignKey('PostcodeMapping')

    class Meta:
        ordering = ('postcode', 'address_1')

    def __unicode__(self):
        return "".join([unicode(self.getattr(x)) for x in ['address_1', 'address_2', 'address_3', 'city', 'postcode']
                        if self.getattr(x)])


gender_choices = (('M', 'M'), ('F', 'F'))


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey('Address')
    gender = models.CharField(max_length=4, choices=gender_choices)
    email = models.EmailField(max_length=255)


boundary_choices = ((1, 'Council',), (2, 'Scottish Parliamentary Region',), (3, 'Scottish Parliament Constituency'))


class GeographicalBoundary(models.Model):
    name = models.CharField(max_length=255)
    boundary_type = models.IntegerField(choices=boundary_choices)
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()


class Region(models.Model):
    name = models.CharField(max_length=60)
    area_code = models.CharField(max_length=3)
    descriptio = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    number = models.FloatField()
    number0 = models.FloatField()
    polygon_id = models.FloatField()
    unit_id = models.FloatField()
    code = models.CharField(max_length=9)
    hectares = models.FloatField()
    area = models.FloatField()
    type_code = models.CharField(max_length=2)
    descript0 = models.CharField(max_length=25)
    type_cod0 = models.CharField(max_length=3)
    descript1 = models.CharField(max_length=36)
    geom = models.MultiPolygonField(srid=27700)
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s: %s" % (self.name, self.descriptio)

    @staticmethod
    def fill_up_db(shapefile, verbose=False):
        from django.contrib.gis.utils import LayerMapping

        mapping = {
            'name': 'NAME',
            'area_code': 'AREA_CODE',
            'descriptio': 'DESCRIPTIO',
            'file_name': 'FILE_NAME',
            'number': 'NUMBER',
            'number0': 'NUMBER0',
            'polygon_id': 'POLYGON_ID',
            'unit_id': 'UNIT_ID',
            'code': 'CODE',
            'hectares': 'HECTARES',
            'area': 'AREA',
            'type_code': 'TYPE_CODE',
            'descript0': 'DESCRIPT0',
            'type_cod0': 'TYPE_COD0',
            'descript1': 'DESCRIPT1',
            'geom': 'POLYGON',
        }
        lm = LayerMapping(Region, shapefile, mapping,
                          transform=False, encoding='iso-8859-1')
        lm.save(strict=True, verbose=verbose)