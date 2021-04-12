from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_authors, name="get_all_authors"),
    path('new_author', views.author_form, name="new_author"),
    path('<int:id>', views.get_author, name="get_author"),
    path('delete_author/<int:id>', views.delete_author, name="delete_author"),
    path('edit_author/<int:id>', views.author_form, name="edit_author")
]
