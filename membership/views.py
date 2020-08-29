from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib import messages
from django.urls import reverse
from .models import Membership, UserMembership, Subscription
# Create your views here.


def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


class MembershipView(ListView):
    model = Membership

    def get_content_data(self, *args, **kwargs):
        context = super().get_content_data(**kwargs)
        current_membership = self.get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self, request, **kwargs):
        selected_membership = request.POST.get('membership_type')
        user_membership = get_user_membership(request)
        user_subscription = get_user_subscription(request)

        select_membership_qs = Membership.objects.filter(
            membership_type=selected_membership
        )
        if select_membership_qs.exists():
            selected_membership = select_membership_qs.first()

        if user_membership.membership == selected_membership:
            if user_subscription != None:
                messages.info(request, "You are currently signed up to this membership")
            return HttpResponseRedirect(request.meta.get('HTTP_REFERER'))

        request.session['selected_mebership_type'] = selected_membership.membership_type

        return HttpResponseRedirect(reverse('membership:payment'))
