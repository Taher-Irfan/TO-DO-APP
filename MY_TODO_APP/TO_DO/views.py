from django.shortcuts import render
from .models import Todo


def home(request):
    data = Todo.objects.all()
    print(data)
    return render(request, 'main/index.html', {'data': data})


def search(request):
    data = request.POST.get('search')
    task = Todo.objects.create(text=data)
    task.save()
    data = Todo.objects.all()
    return render(request, 'main/index.html', {'data': data})


def delete(request, t_id):
    print("first print")
    to_do = Todo.objects.get(pk=t_id)
    print("here delete me")
    to_do.delete()
    data = Todo.objects.all()
    return render(request, 'main/index.html', {'data': data})



