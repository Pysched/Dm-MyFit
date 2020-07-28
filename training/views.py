from django.shortcuts import render


def training(request):
    """ A view to return the training page """
    return render(request, 'training/training.html')
