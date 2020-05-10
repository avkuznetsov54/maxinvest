from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CommercialPremises
from .serializers import CommercialPremisesListSerializer, CommercialPremisesDetailSerializer


class CommercialPremisesListView(APIView):

    def get(self, request):
        premises = CommercialPremises.objects.all() \
            .select_related('region', 'city', 'district', 'residential_complex') \
            .prefetch_related('cooker_hood', 'fixed_agent', 'floor', 'relative_location', 'purpose_commercial_premise',
                              'business_category', 'communication_systems', 'type_entrance') \
            .prefetch_related('images_commercial_premises', 'floorplans_commercial_premises',
                              'video_commercial_premises')

        serializer = CommercialPremisesListSerializer(premises, many=True)
        return Response(serializer.data)


class CommercialPremisesDetailView(APIView):

    def get(self, request, pk):
        premises = CommercialPremises.objects \
            .select_related('region', 'city', 'district', 'residential_complex') \
            .get(id=pk)

        serializer = CommercialPremisesDetailSerializer(premises)
        return Response(serializer.data)
