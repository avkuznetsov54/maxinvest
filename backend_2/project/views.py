from rest_framework.response import Response
from rest_framework.views import APIView

from commercial_real_estate.models import TypeCommercialEstate, BusinessCategory
from .serializers import FiltersSerializers


class FiltersView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}
        filters['type_commercial_estate'] = TypeCommercialEstate.objects.all()
        filters['business_category'] = BusinessCategory.objects.all()

        serializer = FiltersSerializers(filters)
        return Response(serializer.data)
