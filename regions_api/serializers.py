
from .models import  Region
from rest_framework import serializers
   
class RegionSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = Region
        fields = "__all__"
       

    def create(self, validated_data):
        return Region.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.region_name = validated_data.get('region_name', instance.region_name)
        instance.county_name = validated_data.get('county_name', instance.county_name)
        instance.city_town = validated_data.get('city_town', instance.city_town)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance