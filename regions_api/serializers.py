from rest_framework.serializers import ModelSerializer
from .models import  Region


class RegionNestedSerializer(ModelSerializer):
    
    class Meta:
        fields = "__all__"
        read_only_fields = ['region_name', 'county_name', ]
        model = Region

   
class RegionSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        read_only_fields = ['region_name', 'county_name']
        model = Region