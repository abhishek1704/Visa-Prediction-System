from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visaForm/', views.visaForm, name='visaForm'),
    path('h1bFirst', views.h1bFirst, name='h1bFirst'),
    path('h1bSecond', views.h1bSecond, name='h1bSecond'),
    path('h1bSubmit', views.h1bSubmit, name='h1bSubmit'),

    # path('Applications', views.DisplayApplications, name='DisplayApplications'),
    # path('Applications', views.DisplayApplications, name='DisplayApplications'),
    # path('Applications', views.DisplayApplications, name='DisplayApplications')

]
