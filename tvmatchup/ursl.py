from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ListCreateTemplate.as_view(), name='temp_list'),

    path('<int:template_pk>/matchup/', views.ListCreateMatchup.as_view(), name='match_list'),

    path('<int:pk>/template/', views.RetrieveUpdateDestroyTemplate.as_view()),

    path('<int:template_pk>/matchup/<int:pk>/', views.RetrieveUpdateDestroyMatchup.as_view()),

    # url('', views.template_list)



]