from . import views
from django.urls import path
urlpatterns = [

    path('', views.homepage_view, name='homepage')
    

]