from django_filters import rest_framework as filters
from .models import Region

class RegionFilter(filters.FilterSet):
    class Meta:
        model = Region
        fields = ['region_name', 'city_town', 'status']