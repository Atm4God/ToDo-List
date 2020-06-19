from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect
                              )
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm


@login_required()
def index(request):
    # todo_list = Todo.objects.order_by('id')
    todo_list = request.user.todo_list.all().order_by('id')
    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
        request.user.todo_list.add(new_todo)
    return redirect('todo-index')


def complete_todo(request, todo_id):
    todo = request.user.todo_list.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('todo-index')


def delete_completed(request):
    request.user.todo_list.filter(complete__exact=True).delete()
    return redirect('todo-index')


def delete_all(request):
    request.user.todo_list.all().delete()
    return redirect('todo-index')

# # delete view for details
# def delete_view(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context = {}
#     # fetch the object related to passed id
#     obj = get_object_or_404(Todo, pk=id)
#
#     if request.method == "POST":
#         # delete object
#         obj.delete()
#         # after deleting redirect to
#         # home page
#         return HttpResponseRedirect("/")
#
#     return render(request, "delete_view.html", context)
