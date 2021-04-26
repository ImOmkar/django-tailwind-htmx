from django.urls import path
from .views import home, delete_task, create_task, update_task

urlpatterns = [
    path('', home, name="home"),
    path('tasks/create/', create_task, name="create_task"),
    path('tasks/<int:id>/update/', update_task, name="update_task"),
    path('tasks/<int:id>/delete/', delete_task, name="delete_task"),
    
]
