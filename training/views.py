from django.shortcuts import render



def training(request):
    """ A view to return the index page """
    return render(request, 'training/base.html')