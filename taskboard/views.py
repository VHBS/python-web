from django.shortcuts import render
from .models import Board, Tasks
from .serializer import BoardSerializer, TasksSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


def index(request):
    context = {
        'minha_chave': Board.objects.all()
    }
    return render(request, 'index.html', context)

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    @action(detail=False)
    def pending(self, request):
        queryset = Tasks.objects.all().filter(status="Pending")
        serializer = TasksSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False)
    def doing(self, request):
        queryset = Tasks.objects.all().filter(status="Doing")
        serializer = TasksSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False)
    def done(self, request):
        queryset = Tasks.objects.all().filter(status="Done")
        serializer = TasksSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)