from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from main.models import TodoItem

# Create your views here.
def getGreeting(request):
    greetings = "Hello World!"
    items = TodoItem.objects.all()
    if items.exists():
        return redirect('/items/')
    
    return render(request, 'home.html', {'greetings': greetings})


def getItems(request):
    todo_items = TodoItem.objects.all()
    
    return render(request, 'home.html', {'todo_items': todo_items})  


@require_http_methods(["POST"])
def addItem(request):
    name = request.POST.get('name')
    todo_item = TodoItem.objects.create(name=name)
    todo_item.save()

    return redirect('/items/')


def updateItem(request, id):
    item = TodoItem.objects.get(id=id)
    item.completed = True
    item.save()
    
    return redirect('/items/')

def deleteItem(request, id):
    item = TodoItem.objects.get(id=id)
    # item.delete() 
    # Here we are using soft deletion
    item.is_deleted = True
    item.save()
    
    return redirect('/items/')
