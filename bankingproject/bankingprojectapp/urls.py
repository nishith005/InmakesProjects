from django.urls import path
from . import views
app_name='bankingprojectapp'

urlpatterns = [
    path('', views.indes, name='index'),

    ]