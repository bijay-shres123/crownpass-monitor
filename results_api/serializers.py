
from results_api.models import Result
from rest_framework import serializers
# from regions_api.serializers import RegionSerializer

class ResultsSerializer(serializers.ModelSerializer):
    """Serializes a user Test object"""
    

    class Meta:
        model = Result
        fields = "__all__"
    

    def create(self, validated_data):
        return Result.objects.create(**validated_data)

    def Test(self, instance, validated_data):
        instance.number_of_positive = validated_data.get('number_of_positive', instance.number_of_positive)
        instance.number_of_recovered = validated_data.get('number_of_recovered', instance.number_of_recovered)
        instance.number_of_negative = validated_data.get('number_of_negative', instance.number_of_negative)
        instance.date = validated_data.get('date', instance.date)
        instance.region = validated_data.get('region', instance.region)
        instance.save()
        return instance

