"""myfit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('training/', include('training.urls')),
    path('products/', include('products.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('blog/', include('blog.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
<<<<<<< HEAD
    path('contact/', include('contact.urls')),
=======
    path('courses/', include('courses.urls', namespace='courses')),
    path('membership/', include('membership.urls', namespace='memberships')),
<<<<<<< HEAD
>>>>>>> parent of a8b57e7... create contact us app, setup of models, urls, views and html, reworked requirements as alot ad not taken affect
=======
>>>>>>> parent of 139ae00... edited templates for allauth as styling has broken for some unknow reason
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
