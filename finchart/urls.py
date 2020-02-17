from django.urls import path

from . import views

app_name = 'finchart'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
]