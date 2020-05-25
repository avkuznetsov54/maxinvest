from django.urls import path, include

from .views import CommercialEstateListView, CommercialEstateDetailView


urlpatterns = [
    path('estate/all/', CommercialEstateListView.as_view()),
    path('estate/<int:pk>/', CommercialEstateDetailView.as_view()),
]
