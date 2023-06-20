from django.urls import path
from stores import views

app_name = 'stores'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_employee/', views.add_employee, name="add_employee"),
    path('remove_employee/', views.remove_employee, name="remove_employee"),
]
