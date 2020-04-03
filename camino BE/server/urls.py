from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('details/', views.create_record, name='create_record'),
    path('login/', views.login, name='login'),
    url(r'^api-auth/', include('rest_framework.urls'))
]