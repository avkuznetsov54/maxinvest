import re
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination

from .models import CommercialEstate
from .serializers import CommercialEstateListSerializer, CommercialEstateDetailSerializer

from .custom_checks import is_list_int, is_int

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
        print('вход queryset =>', self.request.query_params)
        # for k, v in self.request.query_params.items():
        #     params = {}
        #     # if k == "cursor":
        #     #     continue
        #
        #     # если 'v' равно пустой строке то прекращаем итерацию что не занести её в queryset, а то 500 error
        #     if v == '':
        #         continue
        #     if k == 'is_sale':
        #         if v == 'true':
        #             params.update({k: True})
        #     if k == 'is_rent':
        #         if v == 'true':
        #             params.update({k: True})
        #     if k == 'typeComEstate':
        #         k = 'type_commercial_estate__name' + '__in'
        #         v = v.split(',')
        #         params.update({k: v})
        #     if k == 'purchaseMethod':
        #         k = 'purchase_method__name' + '__in'
        #         v = v.split(',')
        #         params.update({k: v})
        #     if k == 'minCost':
        #         v = re.sub("\D", "", v)
        #         if v == '':
        #             continue
        #         k = 'cost_of_sale' + '__gte'
        #         params.update({k: v})
        #     if k == 'maxCost':
        #         v = re.sub("\D", "", v)
        #         if v == '':
        #             continue
        #         k = 'cost_of_sale' + '__lte'
        #         params.update({k: v})
        #     if k == 'minRent':
        #         v = re.sub("\D", "", v)
        #         if v == '':
        #             continue
        #         k = 'rent_price_month' + '__gte'
        #         params.update({k: v})
        #     if k == 'maxRent':
        #         v = re.sub("\D", "", v)
        #         if v == '':
        #             continue
        #         k = 'rent_price_month' + '__lte'
        #         params.update({k: v})
        #
        #     print(params)
        #     queryset = queryset.filter(**params)

        params = []
        for k, v in self.request.query_params.items():
            # if k == "cursor":
            #     continue

            # если 'v' равно пустой строке то прекращаем итерацию что не занести её в queryset, а то 500 error
            if v == '':
                continue

            if k == 'is_sale':
                if v == 'true':
                    params.append(Q(is_sale=True))

            if k == 'is_rent':
                if v == 'true':
                    params.append(Q(is_rent=True))

            if k == 'checkSale':
                if v == 'true':
                    params.append(Q(is_sale=True))

            if k == 'checkRent':
                if v == 'true':
                    params.append(Q(is_rent=True))

            if k == 'typeComEstate':
                v = v.split(',')
                n = is_list_int(v)
                if len(n) != 0:
                    params.append(Q(type_commercial_estate__in=n))

            if k == 'purchaseMethod':
                v = v.split(',')
                params.append(Q(purchase_method__in=v))

            if k == 'minCost':
                v = is_int(v)
                if v:
                    params.append(Q(cost_of_sale__gte=v))

            if k == 'maxCost':
                v = re.sub("\D", "", v)
                if v == '':
                    continue
                params.append(Q(cost_of_sale__lte=v))

            if k == 'minRent':
                v = re.sub("\D", "", v)
                if v == '':
                    continue
                params.append(Q(rent_price_month__gte=v))
            if k == 'maxRent':
                v = re.sub("\D", "", v)
                if v == '':
                    continue
                params.append(Q(rent_price_month__lte=v))

            if k == 'businessCategory':
                v = v.split(',')
                params.append(Q(business_category__in=v))

        print('params =>', params)
        queryset = queryset.filter(*params)

        return queryset.distinct()


class CommercialEstateDetailView(APIView):

    def get(self, request, pk):
        premises = CommercialEstate.objects \
            .select_related('region', 'city', 'district', 'address', 'business_center', 'residential_complex') \
            .get(id=pk)

        serializer = CommercialEstateDetailSerializer(premises)
        return Response(serializer.data)
