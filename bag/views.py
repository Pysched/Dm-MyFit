from django.shortcuts import render


def view_bag(request):
    """ A view to return the Shopping bag """
    return render(request, 'bag/bag.html')
