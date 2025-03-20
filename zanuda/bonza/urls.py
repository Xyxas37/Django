
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('data', views.data),
    path('test', views.test),
    path('works/', views.works, name='works'),  # Работы
    path('contacts/', views.contacts, name='contacts'),  # Контакты
    path('payments/', views.payments, name='payments'),  # Формы оплаты
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
