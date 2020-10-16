from django.shortcuts import render, get_object_or_404 
from .models import Questions
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

def questionView(request):
    posts = Questions.objects.all() 
    return render(request, 'testgateway/show.html', {'posts': posts})


@require_POST
def questionFilterView(request):
    questionId = request.POST.get('questionId')
    filteredQuestion = Questions.objects.filter(pk = int(questionId))
    serData = serialize('json', filteredQuestion) 
    return JsonResponse({'desiredQuestion' : serData , 'status' : 'ok'})



