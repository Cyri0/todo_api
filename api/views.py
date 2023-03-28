from django.http import JsonResponse
from .models import TodoItem
from .serializers import TodoItemSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def base(request):
    return Response(
        {
            "This page":"/",
            "All ToDos":"todos/",
            "Todo By ID":"todo/<int:id>",
            "Create new item": "create-todo/",
        }
    )

@api_view(['GET'])
def getTodos(request):
    items = TodoItem.objects.all()
    serializer = TodoItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTodoById(request, id):
    try:
        item = TodoItem.objects.get(id=id)
        serializer = TodoItemSerializer(item, many = False)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)})

@api_view(['POST'])
def createTodo(request):
    serializer = TodoItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response({"message":"Success!"})


@api_view(['PUT'])
def updateTodo(request,id):

    try:
        item = TodoItem.objects.get(id=id)
        serializer = TodoItemSerializer(instance=item, data=request.data)

        if serializer.is_valid():
            serializer.save()
        
        return Response({"message":"Success!"})

    except Exception as e:
        return Response({"message": str(e)})


@api_view(['DELETE'])

def deleteTodo(request, id):
    item = TodoItem.objects.get(id=id)
    serializer = TodoItemSerializer(instance=item)
    item.delete()

    return Response(serializer.data)