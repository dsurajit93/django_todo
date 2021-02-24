from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def dashboard(request):
    user = request.user
    tasks = Task.objects.filter(user=user).order_by(
        'is_completed', 'date', 'time')
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/dashboard.html', context)


def add_task(request):
    if request.method == "POST":
        user = request.user
        task = request.POST['task']
        date = request.POST['date']
        time = request.POST['time']

        task = Task(user=user, task=task, date=date, time=time)
        task.save()

        return redirect('dashboard')


def change_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = False if task.is_completed else True
    task.save()
    return redirect('dashboard')


def get_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {
        'update_task': task,
    }
    return render(request, 'tasks/update_task.html', context)


def post_edit(request):
    if request.method == "POST":
        task_id = request.POST['task_id']
        new_task = request.POST['task']
        date = request.POST['date']
        time = request.POST['time']

        task = get_object_or_404(Task, pk=task_id)
        task.task = new_task
        task.date = date
        task.time = time

        task.save()
        return redirect('dashboard')

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('dashboard')
    
def search(request):
    if request.method == "POST":
        date = request.POST['date']
        user = request.user

        tasks = Task.objects.filter(user=user, date=date)

        context = {
            'date' : date,
            'tasks' : tasks
        }
        return render(request, 'tasks/dashboard.html', context)
