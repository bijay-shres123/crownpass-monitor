
from results_api.models import Results
from rest_framework import serializers
# from regions_api.serializers import RegionSerializer

class ResultsSerializer(serializers.ModelSerializer):
    """Serializes a user Test object"""
    

    class Meta:
        model = Results
        fields = "__all__"
    

    def create(self, validated_data):
        return Results.objects.create(**validated_data)

    def Test(self, instance, validated_data):
        instance.number_of_positive = validated_data.get('number_of_positive', instance.number_of_positive)
        instance.number_of_recovered = validated_data.get('number_of_recovered', instance.number_of_recovered)
        instance.number_of_negative = validated_data.get('number_of_negative', instance.number_of_negative)
        instance.date = validated_data.get('date', instance.date)
        instance.region = validated_data.get('region', instance.region)
        instance.save()
        return instance

