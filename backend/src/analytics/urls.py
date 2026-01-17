from django.urls import path
from .views import AnalyticsOverviewAPIView

urlpatterns = [
    path('overview/',AnalyticsOverviewAPIView.as_view(), name= 'analytics_overview'),
]