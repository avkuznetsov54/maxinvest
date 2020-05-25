from rest_framework import serializers

from commercial_real_estate.models import TypeCommercialEstate, BusinessCategory


class TypeCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCommercialEstate
        fields = ('id', 'name')


class BusinessCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ('id', 'name')


class FiltersSerializers(serializers.Serializer):
    type_commercial_estate = TypeCommercialEstateListSerializer(read_only=True, many=True)
    business_category = BusinessCategoryListSerializer(read_only=True, many=True)
    # model_2 = Model2Serializers(read_only=True)
    # model_3 = Model3Serializers(read_only=True)
