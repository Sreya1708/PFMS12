from django.urls import path, include
from . import views

app_name = 'managerapp'


urlpatterns = [
    path('managerhomepage/', views.managerhomepage, name='managerhomepage'),
]