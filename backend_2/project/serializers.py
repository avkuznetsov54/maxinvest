from rest_framework import serializers

from geo_location.models import City, District, Street
from residential_real_estate.models import NamesOfMetroStations, ResidentialComplex, ClassOfHousing
from commercial_real_estate.models import (TypeCommercialEstate, BusinessCategory, RelativeLocation, FinishingProperty,
                                           CommunicationSystems, CookerHood, TypeEntranceToCommercialEstate)


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class StreetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'name')


class TypeCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCommercialEstate
        fields = ('id', 'name')


class BusinessCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ('id', 'name')


class RelativeLocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelativeLocation
        fields = ('id', 'name')


class NamesOfMetroStationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamesOfMetroStations
        fields = ('id', 'name')


class FinishingPropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishingProperty
        fields = ('id', 'name')


class CommunicationSystemsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationSystems
        fields = ('id', 'name')


class CookerHoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookerHood
        fields = ('id', 'name')


class TypeEntranceToCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEntranceToCommercialEstate
        fields = ('id', 'name')


class ResidentialComplexListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialComplex
        fields = ('id', 'name')


class ClassOfHousingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassOfHousing
        fields = ('id', 'name')


class FiltersSerializers(serializers.Serializer):
    city = CityListSerializer(read_only=True, many=True)
    district = DistrictListSerializer(read_only=True, many=True)
    street = StreetListSerializer(read_only=True, many=True)
    type_commercial_estate = TypeCommercialEstateListSerializer(read_only=True, many=True)
    business_category = BusinessCategoryListSerializer(read_only=True, many=True)
    relative_location = RelativeLocationListSerializer(read_only=True, many=True)
    metro_stations = NamesOfMetroStationsListSerializer(read_only=True, many=True)
    finishing_property = FinishingPropertyListSerializer(read_only=True, many=True)
    communication_systems = CommunicationSystemsListSerializer(read_only=True, many=True)
    cooker_hood = CookerHoodListSerializer(read_only=True, many=True)
    type_entrance = TypeEntranceToCommercialEstateListSerializer(read_only=True, many=True)
    residential_complex = ResidentialComplexListSerializer(read_only=True, many=True)
    class_of_housing = ClassOfHousingListSerializer(read_only=True, many=True)


