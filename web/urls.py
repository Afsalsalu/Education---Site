from django.contrib import admin
from django.urls import path,include
from . views import IndexView 
from . import views
from .views import seccess1_view
from .views import Contact
app_name='web'
urlpatterns = [
   path("",IndexView.as_view(),name='index'),
   path("contact",views.Contact ,name="contact"),
   path('seccess1/',views.seccess1_view, name='seccess1/')
   
]