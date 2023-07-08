from django.urls import path
from users import views

app_name = 'users'


urlpatterns = [
    path('', views.index, name="index"),
    path('add_user/', views.add_user, name="add_user"),
    path('update_user/<int:_id>/', views.update_user, name="update_user"),
    path('remove_user/<int:_id>/', views.remove_user, name="remove_user")
]
