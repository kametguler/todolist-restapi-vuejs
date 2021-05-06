from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def List(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DetailView(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateView(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UpdateView(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteView(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()

    return Response()


