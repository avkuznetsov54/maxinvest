from django.urls import path, include

from .views import CommercialPremisesListView, CommercialPremisesDetailView


urlpatterns = [
    path('premises/all/', CommercialPremisesListView.as_view()),
    path('premises/<int:pk>/', CommercialPremisesDetailView.as_view()),
]
