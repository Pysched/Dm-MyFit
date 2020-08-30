from django.shortcuts import render


def nutrition(request):
    """ A view to return the Nutrition page """
    return render(request, 'nutrition/nutrition.html')
