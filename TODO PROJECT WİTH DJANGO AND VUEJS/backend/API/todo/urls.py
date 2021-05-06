from django.urls import path
from .views import apiOverview, List, DetailView, CreateView, DeleteView, UpdateView

urlpatterns = [
    path('', apiOverview, name="apiOverview"),
    path('task-list/', List, name="taskList"),
    path('task-detail/<str:pk>', DetailView, name="taskDetail"),
    path('task-create/', CreateView, name="taskCreate"),
    path('task-update/<str:pk>', UpdateView, name="taskUpdate"),
    path('task-delete/<str:pk>', DeleteView, name="taskDelete"),

]