from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactUsForm


def contactus_form(request):
    "A view to return the contact page"
    contactus_form = ContactUsForm()
    if request.method == 'POST':
        contactus_form = ContactUsForm(request.POST)
        if contactus_form.is_valid:
            contactus_form.save()
            messages.success(request, 'Thank you for getting in touch!\
                 We will be in touch as soon as possible.')
            return redirect('contactus')

    template = 'contactus/contactus.html'
    context = {
        'contactus_form': contactus_form,
        'on_profile_page': True
    }

    return render(request, template, context)
