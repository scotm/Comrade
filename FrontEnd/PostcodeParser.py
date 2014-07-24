# coding=utf-8
from abc import abstractmethod
from django.contrib.gis.geos import Point
from FrontEnd.models import PostcodeMapping

__author__ = 'scotm'


class PostCodeProcessor(object):
    @abstractmethod
    def process_postcode(self, line):
        raise NotImplementedError


class BritishPostCodeProcessor(PostCodeProcessor):
    def process_postcode(self, line):
        line['point'] = Point(float(line['longitude']), float(line['latitude']))
        del line['longitude']
        del line['latitude']
        return PostcodeMapping(**line)