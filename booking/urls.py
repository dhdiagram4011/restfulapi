from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('booking/', BookingList.as_view()),
    path('booking/<int:pk>/', BookingDetail.as_view()),
    path('bookingall/', bookingall, name='bookingall'),
]


