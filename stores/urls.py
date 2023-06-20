from django.urls import path
from stores import views

app_name = 'stores'

urlpatterns = [
    path('', views.index, name="index"),
]
