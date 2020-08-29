from django.urls import path, include
from .views import MembershipView, PaymentView


app_name = 'membership'

urlpatterns = [
    path('', MembershipView.as_view(), name='select'),
    path('payment', PaymentView, name='payment'),
]
