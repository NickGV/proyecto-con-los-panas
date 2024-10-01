from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, task_complete

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/complete/', task_complete, name='task_complete'),
]
