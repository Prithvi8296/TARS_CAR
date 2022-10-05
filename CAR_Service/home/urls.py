from xml.etree.ElementInclude import include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   path('aboutus/',views.aboutus,name="aboutus"),
   path('offers/',views.offers,name="offers"),
   path('doorstep/',views.doorstep,name="doorstep"),
   path('contactus/',views.contactus,name="contactus"),
   path('login/',views.login,name="login"),
   path('login/register/',views.register,name="register"),
   path('services/',views.services,name="services"),
   
   
]
urlpatterns += staticfiles_urlpatterns() 
