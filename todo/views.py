from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    form = TodoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "todo/home.html", {"form": form, "todos": todos})



def todos(request):
    todos = Todo.objects.all()
    return render(request, "todo/partials/todos_list.html", {"todos": todos})


def contact(request):
    return render(request, "todo/contact.html")


def complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = Todo.objects.all()
    return render(request, "todo/partials/todos_list.html", {"todos": todos})