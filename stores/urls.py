from django.urls import path
from stores import views

app_name = 'stores'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_product/', views.add_product, name="add_product"),
    path('remove_product/<int:_id>', views.remove_product, name="remove_product"),
    path('update_product/<int:_id>', views.update_product, name="update_product"),
    path('all_employees/', views.all_employees, name="all_employees"),
    path('add_employee/', views.add_employee, name="add_employee"),
    path('employee_detail/<int:_id>/',
         views.employee_detail, name="employee_detail"),
    path('remove_employee/<int:_id>/',
         views.remove_employee, name="remove_employee"),
    path('update_employee/<int:_id>/',
         views.update_employee, name="update_employee"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
