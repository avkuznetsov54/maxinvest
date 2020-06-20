from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination

from .models import CommercialEstate
from .serializers import CommercialEstateListSerializer, CommercialEstateDetailSerializer


# class CommercialEstateListView(APIView):
#
#     def get(self, request):
#         premises = CommercialEstate.objects.all() \
#             .select_related('region', 'city', 'district', 'address', 'business_center', 'residential_complex') \
#             .prefetch_related('metro_stations', 'cooker_hood', 'fixed_agent', 'floor', 'relative_location',
#                               'type_commercial_estate', 'business_category', 'communication_systems', 'type_entrance',
#                               'finishing_property', 'purchase_method') \
#             .prefetch_related('images_commercial_estate', 'floorplans_commercial_estate',
#                               'video_commercial_estate')
#
#         serializer = CommercialEstateListSerializer(premises, many=True)
#         return Response(serializer.data)


class CommerceListPagination(PageNumberPagination):
    page_size = 20


class CommercialEstateListView(generics.ListAPIView):
    serializer_class = CommercialEstateListSerializer
    queryset = CommercialEstate.objects.filter(is_active=True) \
        .select_related('region', 'city', 'district', 'address', 'business_center', 'residential_complex') \
        .prefetch_related('metro_stations', 'cooker_hood', 'fixed_agent', 'floor', 'relative_location',
                          'type_commercial_estate', 'business_category', 'communication_systems', 'type_entrance',
                          'finishing_property', 'purchase_method') \
        .prefetch_related('images_commercial_estate', 'floorplans_commercial_estate',
                          'video_commercial_estate')
    pagination_class = CommerceListPagination

    def filter_queryset(self, queryset):
        # print(self.request.query_params)
        for k, v in self.request.query_params.items():
            params = {}
            # if k == "cursor":
            #     continue

            # если 'v' равно пустой строке то прекращаем итерацию что не занести её в queryset, а то 500 error
            if v == '':
                continue
            if k == 'is_sale':
                if v == 'true':
                    params.update({k: True})
            if k == 'is_rent':
                if v == 'true':
                    params.update({k: True})
            if k == 'typeComEstate':
                k = 'type_commercial_estate__name' + '__in'
                v = v.split(',')
                # print(v)
                params.update({k: v})

            # print(params)
            queryset = queryset.filter(**params)

        return queryset.distinct()


class CommercialEstateDetailView(APIView):

    def get(self, request, pk):
        premises = CommercialEstate.objects \
            .select_related('region', 'city', 'district', 'address', 'business_center', 'residential_complex') \
            .get(id=pk)

        serializer = CommercialEstateDetailSerializer(premises)
        return Response(serializer.data)
