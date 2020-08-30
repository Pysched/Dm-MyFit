from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        name = request.POST['name'],
        email = request.POST['email'],
        message = request.POST['message'],

        messages.success(request, 'Thank your for you enquiry!\
            we will endeavour to reply as soon as possible.')

        # to send an email
        # send_mail(
        #     name,  # subject
        #     message,  # message
        #     email,  # from email
        #     ['']  # to email
        # )

        return render(request, 'contact/contact.html', {'name': name})
    else:
        return render(request, 'contact/contact.html', {})
