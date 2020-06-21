from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('contacto',views.contacto),
    path('test1',views.t1),
]
