
from django.urls import path
from . import views


urlpatterns = [

    path('news/', views.news_list, name='news_home'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),

]
