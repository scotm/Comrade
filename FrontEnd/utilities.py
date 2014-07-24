__author__ = 'scotm'
import time
import csv

from models import PostcodeMapping
from django.contrib.gis.geos import Point


def process_postcode_data(line):
    return PostcodeMapping(postcode=line['postcode'],
                           point=Point(float(line['longitude']), float(line['latitude'])))


def postcode_chunks(reader, length):
    postcodes = []
    for line in reader:
        postcodes.append(process_postcode_data(line))
        if len(postcodes) == length:
            yield postcodes
            postcodes = []
    yield postcodes


def fill_up_db(postcode_filename, chunk_size=5):
    start_time = time.time()
    i = 0
    with open(postcode_filename) as myfile:
        # Read in the postcodes file - and remove duplicates
        print "Reading in postcode file"
        reader = csv.DictReader(myfile)
        chunker = postcode_chunks(reader, chunk_size)
        failed_chunks = []
        for chunk in chunker:
            try:
                PostcodeMapping.objects.bulk_create(chunk)
            except:
                failed_chunks += chunk
                continue
            i += len(chunk)
            print "%d records written over %f seconds" % (i, time.time() - start_time)

    for i in failed_chunks:
        try:
            print "Trying %s" % i.postcode
            i.save()
        except:
            print "%s failed" % unicode(i)