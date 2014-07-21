import floppyforms.__future__ as forms

__author__ = 'scotm'
from django.contrib import admin
from FrontEnd.models import PostcodeMapping, Address, Person, GeographicalBoundary, Region


class PostcodeAdmin(admin.ModelAdmin):
    search_fields = ('postcode',)
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


class GMapPointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
    pass


class GMapMultiPolygonWidget(forms.gis.MultiPolygonWidget, forms.gis.BaseGMapWidget):
    pass


class RegionWidget(GMapMultiPolygonWidget):
    map_srid = 27700


class RegionAdminForm(forms.ModelForm):
    model = Region

    class Meta:
        widgets = {
            'geom': RegionWidget,
        }


class RegionAdmin(admin.ModelAdmin):
    list_filter = ('descriptio',)
    search_fields = ('name',)
    form = RegionAdminForm


admin.site.register(PostcodeMapping, PostcodeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(GeographicalBoundary, admin.ModelAdmin)
admin.site.register(Region, RegionAdmin)