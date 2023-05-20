from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('newpage', views.new_page, name='newpage'),
    path('formpage', views.form_page, name='formpage'),
    path('logout',views.logout,name='logout'),
    path('finalpage',views.final_page,name='finalpage'),
    path('backtohome',views.back_to_home,name='backtohome'),
    path('district_wikipedia/<str:district>/', views.wiki_page, name='wikipage'),
]