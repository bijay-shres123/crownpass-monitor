
import results_api
from results_api.models import Result
from .models import  Region
from rest_framework import serializers
from results_api.serializers import ResultsSerializer

class RegionSerializer(serializers.ModelSerializer):
    """Serializes a user Region object"""

    results =  ResultsSerializer(many= True, read_only = True)

    class Meta:
        model = Region
        fields = ['id','region_name','county_name','city_town','status','results']
       

    def create(self, validated_data):
        return Region.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.region_name = validated_data.get('region_name', instance.region_name)
        instance.county_name = validated_data.get('county_name', instance.county_name)
        instance.city_town = validated_data.get('city_town', instance.city_town)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
