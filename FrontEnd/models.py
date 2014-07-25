# coding=utf-8
from urlparse import urljoin

import re
import requests
from BeautifulSoup import NavigableString, BeautifulSoup
from django.contrib.gis.db import models

postcode_regex = 'GIR[ ]?0AA|((AB|AL|B|BA|BB|BD|BH|BL|BN|BR|BS|BT|BX|CA|CB|CF|CH|CM|CO|CR|CT|CV|CW|DA|DD|DE|DG|DH|DL|DN|DT|DY|E|EC|EH|EN|EX|FK|FY|G|GL|GY|GU|HA|HD|HG|HP|HR|HS|HU|HX|IG|IM|IP|IV|JE|KA|KT|KW|KY|L|LA|LD|LE|LL|LN|LS|LU|M|ME|MK|ML|N|NE|NG|NN|NP|NR|NW|OL|OX|PA|PE|PH|PL|PO|PR|RG|RH|RM|S|SA|SE|SG|SK|SL|SM|SN|SO|SP|SR|SS|ST|SW|SY|TA|TD|TF|TN|TQ|TR|TS|TW|UB|W|WA|WC|WD|WF|WN|WR|WS|WV|YO|ZE)(\\d[\\dA-Z]?[ ]?\\d[ABD-HJLN-UW-Z]{2}))|BFPO[ ]?\\d{1,4}'
prog = re.compile(postcode_regex)


class PostcodeMapping(models.Model):
    postcode = models.CharField(max_length=10, primary_key=True)

    # GeoDjango-specific declarations
    point = models.PointField()
    scraped = models.BooleanField(default=False, db_index=True)
    objects = models.GeoManager()

    def get_addresses(self):
        return AddressRecord.objects.filter(postcode=self)

    def __unicode__(self):
        return self.postcode

    @staticmethod
    def match_postcode(postcode):
        return PostcodeMapping.objects.get(postcode=postcode.replace(' ', ''))


class AddressRecord(models.Model):
    original_data = models.CharField(max_length=512, default='')
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)
    prefix = models.CharField(max_length=50, default='')
    main_door_number = models.CharField(max_length=10, default='')
    city = models.CharField(max_length=50)
    local_authority = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100)
    postcode = models.ForeignKey('PostcodeMapping')
    council_ref = models.CharField(max_length=20, null=True)
    council_tax_band = models.CharField(max_length=5, default='A')

    class Meta(object):
        ordering = ('postcode', 'address_1')

    def __unicode__(self):
        return ", ".join(
            [unicode(x) for x in [self.address_1, self.address_2, self.address_3, self.city, self.postcode] if x])

    @staticmethod
    def add_addresses(postcode):
        postcode_map = PostcodeMapping.match_postcode(postcode)

        def parse_addresses_page(soup):
            addresses, urls = [], []
            main_table = soup.table
            if main_table:
                for row in main_table.findAll('tr')[1:]:  # skip the header-row.
                    elements = row.findAll('td')
                    if len(elements) == 1:
                        urls.append(elements[0].a.get('href'))
                    else:
                        address = AddressRecord()
                        address.postcode = postcode_map
                        address.council_ref = elements[0].text
                        address.council_tax_band = elements[2].text
                        address.local_authority = elements[5].a.text
                        address_lines = [x.strip() for x in elements[1].childGenerator() if
                                         isinstance(x, NavigableString)]
                        address.original_data = repr(address_lines)
                        del address_lines[-1]  # we've already got the postcode
                        address.city = address_lines.pop()
                        address.address_1 = address_lines.pop(0)
                        if address_lines:
                            address.address_2 = address_lines.pop(0)
                            if address_lines:
                                address.address_3 = address_lines.pop(0)
                        addresses.append(address)
            return addresses, urls

        url = "http://www.saa.gov.uk/search.php?SEARCHED=1&SEARCH_TABLE=council_tax&SEARCH_TERM={0:s}+{1:s}&x=0&y=0#results".format(
            postcode[:-3], postcode[-3:])
        print url
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        try:
            urls = [urljoin(url, x.get('href')) for x in soup.find('div', {'class': 'pagecounter'}).findAll('a')]
        except AttributeError:  # there could be no pagecounter div.
            urls = []
        addresses, more_urls = parse_addresses_page(soup)
        urls += [urljoin(url, x) for x in more_urls]
        while urls:
            url = urls.pop()
            print url
            r = requests.get(url)
            soup = BeautifulSoup(r.content)
            more_addresses, more_urls = parse_addresses_page(soup)
            addresses += more_addresses
            urls += [urljoin(url, x) for x in more_urls]
        if addresses:
            print "%d dwelling addresses found for %s" % (len(addresses), postcode)
            AddressRecord.objects.bulk_create(addresses)
        postcode_map.scraped = True
        postcode_map.save()


gender_choices = (('M', 'M'), ('F', 'F'))


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey('AddressRecord')
    gender = models.CharField(max_length=4, choices=gender_choices)
    email = models.EmailField(max_length=255)


boundary_choices = (
(1, 'Council',), (2, 'Scottish Parliamentary Region',), (3, 'Scottish Parliament Constituency'), (4, 'Country'))


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
    geom = models.MultiPolygonField()
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
                          transform=True, encoding='iso-8859-1')
        lm.save(strict=True, verbose=verbose)
        Region.objects.filter(descriptio__icontains='Welsh Assembly').delete()
        print "Regions imported"

        # highlands = Region.objects.filter(name__icontains='Highlands and Islands PER').values('geom')

        # baseline = highlands[0].geom
        # for i in highlands[1:]:
        # baseline = baseline.union(i.geom)
        # Region(name='Highlands and Islands COMPLETE', descriptio='Scottish Parliament Electoral Region', hectares='4050000')
