from django.shortcuts import render, get_object_or_404 
from .models import Questions, Tests, Userstats
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from datetime import timedelta

# Create your views here.

@login_required
def questionView(request):
    posts = Questions.objects.all() 
    return render(request, 'testgateway/show.html', {'posts': posts})

@login_required
def testLandingView(request):
    tests = Tests.objects.all()
    return render(request, 'testgateway/testLanding.html', {'tests' : tests})

@login_required
def testView(request, slug):
    posts = Questions.objects.filter(test__slug=slug)
    return render(request, 'testgateway/show.html', {'posts': posts})



@require_POST
def questionFilterView(request):
    questionId = request.POST.get('questionId')
    #test slug and then
    filteredQuestion = Questions.objects.filter(pk = int(questionId))
    serData = serialize('json', filteredQuestion) 
    return JsonResponse({'desiredQuestion' : serData , 'status' : 'ok'})


@require_POST
def questionSubmitView(request):
    questionId = request.POST.get('questionId')
    #change the name to match whatever in the DB
    submitAns = request.POST.get('submitAns')
    timeTaken = request.POST.get('timeTaken')
    # timeSec = int(timeTaken / 1000)

    tmpUserstats = Userstats.objects.get(userProfile = request.user.profile, questions__id = questionId)
    # prevTimeTaken = tmpUserstats.time.seconds 

    newTime = tmpUserstats.time.seconds + int(int(timeTaken) / 1000)

    # totalTimeTaken = timeSec + prevTimeTaken
    tmpUserstats.submitAnswer = submitAns
    tmpUserstats.time = timedelta(seconds=newTime)
    tmpUserstats.save()
    
    # Userstats.objects.create(userProfile = request.user.profile, questions =  Questions.objects.get(pk = questionId), submitAnswer= submitAns )
    return JsonResponse({'status' : 'ok'})

# @require_POST
# def 
    

