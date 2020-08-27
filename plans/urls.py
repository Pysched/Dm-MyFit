from django.urls import path
from .views import PlanListView, PlanDetailView, LessonDetailView

app_name = 'plans'

urlpatterns = [
    path('', PlanListView.as_view(), name='list'),
    path('<slug>', PlanDetailView.as_view(), name='detail'),
    path('<plan_slug>/<lesson_slug>', LessonDetailView.as_view(), name='lesson-detail')
]
