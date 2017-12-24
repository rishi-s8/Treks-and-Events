from django.urls import path
from . import views

app_name='college'

urlpatterns = [
    path('', views.index, name='index'),
    path('treks/<int:trek_id>/', views.detailsT, name='detailsT'),
    path('events/<int:event_id>/', views.detailsE, name='detailsE'),
]
