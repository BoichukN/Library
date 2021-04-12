from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.get_all_users, name="get_all_users"),
    path('new_user/', views.user_form, name='new_user'),
    path('users/<int:id>/', views.get_by_id, name='get_by_id'),
    path('users/edit_user/<int:id>', views.user_form, name='edit_user'),
    path('delete/<int:delete_id>', views.user_delete, name='user_delete')
]
