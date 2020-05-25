from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CommercialEstate
from .serializers import CommercialEstateListSerializer, CommercialEstateDetailSerializer


class CommercialEstateListView(APIView):

    def get(self, request):
        premises = CommercialEstate.objects.all() \
            .select_related('region', 'city', 'district', 'address', 'residential_complex') \
            .prefetch_related('cooker_hood', 'fixed_agent', 'floor', 'relative_location', 'type_commercial_estate',
                              'business_category', 'communication_systems', 'type_entrance', 'finishing_property') \
            .prefetch_related('images_commercial_estate', 'floorplans_commercial_estate',
                              'video_commercial_estate')

        serializer = CommercialEstateListSerializer(premises, many=True)
        return Response(serializer.data)


class CommercialEstateDetailView(APIView):

    def get(self, request, pk):
        premises = CommercialEstate.objects \
            .select_related('region', 'city', 'district', 'address', 'residential_complex') \
            .get(id=pk)

        serializer = CommercialEstateDetailSerializer(premises)
        return Response(serializer.data)

