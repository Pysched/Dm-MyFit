from django.urls import path
from .views import PlanListView, PlanDetailView

app_name = 'plans'

urlpatterns = [
    path('', PlanListView.as_view(), name='list'),
    path('<slug>', PlanDetailView.as_view(), name='detail'),
]
