from django.shortcuts import render, redirect
from main.models import TodoItem

# Create your views here.
def getGreeting(request):
    pass


def getItems(request):
    todo_items = TodoItem.objects.all()
    
    return render(request, 'home.html', {'todo_items': todo_items})  


def addItem(request):
    name = request.GET.get('name')
    todo_item = TodoItem.objects.create(name=name)
    todo_item.save()

    return redirect('/')


def updateItem(request, id):
    item = TodoItem.objects.get(id=id)
    item.completed = True
    item.save()
    
    return redirect('/')

def deleteItem(request, id):
    item = TodoItem.objects.get(id=id)
    item.delete()
    
    return redirect('/')
