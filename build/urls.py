from django.urls import path
from . import views


urlpatterns =[
    
    # front
    path('', views.index, name='index'),
    path('services', views.services, name='services' ),
    path('ourblogs', views.ourblogs, name='ourblogs'),
    path('contacts', views.contacts, name='contacts' )

]