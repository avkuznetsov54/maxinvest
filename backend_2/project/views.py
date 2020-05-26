from rest_framework.response import Response
from rest_framework.views import APIView

from geo_location.models import City, District, Street
from residential_real_estate.models import NamesOfMetroStations, ResidentialComplex, ClassOfHousing
from commercial_real_estate.models import (TypeCommercialEstate, BusinessCategory, RelativeLocation, FinishingProperty,
                                           CommunicationSystems, CookerHood, TypeEntranceToCommercialEstate,
                                           PurchaseMethod)
from .serializers import FiltersSerializers


class FiltersView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['type_commercial_estate'] = TypeCommercialEstate.objects.all()
        filters['business_category'] = BusinessCategory.objects.all()
        filters['city'] = City.objects.all()
        filters['district'] = District.objects.all()
        filters['street'] = Street.objects.all()
        filters['relative_location'] = RelativeLocation.objects.all()
        filters['metro_stations'] = NamesOfMetroStations.objects.all()
        filters['finishing_property'] = FinishingProperty.objects.all()
        filters['communication_systems'] = CommunicationSystems.objects.all()
        filters['cooker_hood'] = CookerHood.objects.all()
        filters['type_entrance'] = TypeEntranceToCommercialEstate.objects.all()
        filters['residential_complex'] = ResidentialComplex.objects.all()
        filters['class_of_housing'] = ClassOfHousing.objects.all()
        filters['purchase_method'] = PurchaseMethod.objects.all()

        serializer = FiltersSerializers(filters)
        return Response(serializer.data)
