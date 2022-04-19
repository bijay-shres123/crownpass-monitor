
from results_api.models import Results
from rest_framework import serializers

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
        instance.county_name = validated_data.get('county_name', instance.county_name)
        instance.save()
        return instance