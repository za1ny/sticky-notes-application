from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .form import PostForm


# Create your views here.
# Create todo here.
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todos')

    else:
        form = PostForm()

    return render(request, 'todo_form.html', {'form': form})


# Get all todos here - just returns to main page.
def get_all(request):
    todos = Post.objects.all()

    context = {
        'todos': todos,
        'page_title': 'Show all to-do items'
    }

    return render(request, 'all_todo_list.html', context=context)


def get(request, pk):
    todo = get_object_or_404(Post, pk=pk)

    context = {
        'todo': todo
    }

    return render(request, 'todo.html', context=context)


def update(request, pk):
    todo = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=todo)

    if form.is_valid():
        todo = form.save(commit=False)
        todo.save()
        return redirect('todos')

    else:
        form = PostForm()

    return render(request, 'todo_form.html',  {'form': form})


def delete(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    todo.delete()
    return redirect('todos')
