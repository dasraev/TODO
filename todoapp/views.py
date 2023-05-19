from django.shortcuts import render
from django.http import JsonResponse
from . import models

def home(request):
    return render(request,'todoapp/index.html')

def todo_list(request):
    todos = models.Data.objects.all().order_by('date')
    return JsonResponse({'todos':list(todos.values())})


def todo_create(request):
    if request.method == 'POST':
        todo_text = request.POST.get('todo_text')
        todo = models.Data.objects.filter(text=todo_text)

        # we need to make sure that this todo does not exist in the database
        if todo.exists():
            return JsonResponse({'status': 'error'})

        todo = models.Data.objects.create(text=todo_text)
        return JsonResponse({'todo_text': todo.text, 'status': 'created'})

def todo_edit(request):
    if request.method=="POST":
        todo_text=request.POST.get('todo_text')
        new_todo_text=request.POST.get('new_todo_text')
        edited_todo=models.Data.objects.get(text=todo_text)
        if models.Data.objects.filter(text=new_todo_text).exists():
            return JsonResponse({'status':'error-edit'})
        edited_todo.text=new_todo_text
        edited_todo.save()
        context = {
            'new_todo_text':new_todo_text,
            'status':'updated'
        }
        return JsonResponse(context)

def todo_delete(request):
    if request.method == 'POST':
        todo_text = request.POST.get('todo_text')
        models.Data.objects.filter(text=todo_text).delete()
        return JsonResponse({'status': "deleted"})