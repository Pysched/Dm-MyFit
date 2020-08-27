from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from membership.models import UserMembership
from .models import Plans
# Create your views here.


class PlanListView(ListView):
    model = Plans


class PlanDetailView(DetailView):
    model = Plans


class LessonDetailView(View):

    def get(self, request, plan_slug, lesson_slug, *args, **kwargs):

        plan_qs = Plans.objects.filter(slug=plan_slug)
        if plan_qs.exists():
            plan = plan_qs.first()

        lesson_qs = plan.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()


        user_membership = UserMembership.objecst.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type

        plan_allowed_mem_types = plan.allowed_memberships.all()

        context = {
            'object': None
        }

        if plan_allowed_mem_types.filter(memebership_type=user_membership_type).exists():
            context = {'object': lesson}

        return render(request, 'plans/lesson_detail.html', context)
