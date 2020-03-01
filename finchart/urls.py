from django.urls import path

from . import views

app_name = 'finchart'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('company/<int:pk>', views.CompanyView.as_view(), name='company'),
]