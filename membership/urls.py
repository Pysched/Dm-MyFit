from django.urls import path, include
from .views import MembershipView


app_name = 'membership'

urlpatterns = [
    path('', MembershipView.as_view(), name='select'),
]
