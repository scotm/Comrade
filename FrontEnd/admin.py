# coding=utf-8
import floppyforms.__future__ as forms

__author__ = 'scotm'
from django.contrib import admin
from FrontEnd.models import PostcodeMapping, AddressRecord, Person, GeographicalBoundary, Region


class GMapPointWidget(forms.gis.PointWidget, forms.gis.BaseOsmWidget):
    template_name = 'custom_lon_lat.html'
    map_srid = 4326
    default_lon = '0'
    default_lat = '0'

    def get_context_data(self):
        ctx = super(GMapPointWidget, self).get_context_data()
        ctx.update({
            'lon': self.default_lon,
            'lat': self.default_lat,
        })
        return ctx


# class GMapMultiPolygonWidget(forms.gis.MultiPolygonWidget, forms.gis.BaseGMapWidget):
# map_srid = 4326


class PostcodeAdminForm(forms.ModelForm):
    model = PostcodeMapping

    class Meta(object):
        widgets = {
            'point': GMapPointWidget(),
        }


class PostcodeAdmin(admin.ModelAdmin):
    search_fields = ('postcode',)
    form = PostcodeAdminForm


class PersonAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


class RegionAdminForm(forms.ModelForm):
    model = Region

    # class Meta(object):
    #     widgets = {
    #         'geom': GMapMultiPolygonWidget,
    #     }


class RegionAdmin(admin.ModelAdmin):
    list_filter = ('descriptio',)
    search_fields = ('name',)
    form = RegionAdminForm


admin.site.register(PostcodeMapping, PostcodeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(AddressRecord, AddressAdmin)
admin.site.register(GeographicalBoundary, admin.ModelAdmin)
admin.site.register(Region, RegionAdmin)