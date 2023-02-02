from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('latest/',views.get_latest),
    path('<timestamp>/', views.get_latest_data_by_timestamp),
]