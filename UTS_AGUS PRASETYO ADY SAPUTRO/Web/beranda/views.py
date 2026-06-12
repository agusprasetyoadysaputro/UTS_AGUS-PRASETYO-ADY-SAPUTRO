from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'comments': comments})

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment = Comment.objects.create(
            name=data['name'],
            message=data['message']
        )
        return JsonResponse({'id': comment.id, 'name': comment.name, 'message': comment.message})
