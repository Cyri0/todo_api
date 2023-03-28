from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('todos/', views.getTodos),
    path('todo/<int:id>', views.getTodoById),
    path('create-todo/', views.createTodo),
    path('update-todo/<int:id>', views.updateTodo),
    path('delete-todo/<int:id>', views.deleteTodo)
]