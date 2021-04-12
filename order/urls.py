from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_orders, name='get_all_orders'),
    path('<int:id>', views.get_order, name='get_order'),
    path('new_order/', views.order_form, name='new_order'),
    path('delete/<int:id>', views.delete_order, name='delete_order'),
    path('edit_order/<int:id>', views.order_form, name='edit_order')
]
