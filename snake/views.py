import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from snake.forms import EmailUserCreationForm
from snake.models import Score


def home(request):
    return render(request, 'base.html')

@login_required
def snake(request):
    if request.method == "GET":
        high_score = Score.objects.filter(player=request.user)
        highest_score = high_score.aggregate(Max('score'))
        data = {'high_score': high_score, 'highest_score': highest_score}
        return render(request, 'snake.html', data)


def profile(request):
    if request.method == 'GET':
        high_score = Score.objects.filter(player=request.user).order_by('-date')
        highest_score = high_score.aggregate(Max('score'))
        average_score = high_score.aggregate(Avg('score'))
        data = {'high_score': high_score, 'highest_score': highest_score, 'average_score': average_score}
        return render(request, 'profile.html', data)


# Registration view
def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect("home")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@csrf_exempt
def save(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_save = Score.objects.create(
            player=request.user,
            score=data['score'],
            game=data['game'],
        )

        save_info = {
            'player': request.user.username,
            'score': new_save.score,
            'date': new_save.date,
            'game': new_save.game
        }

        return HttpResponse(json.dumps(save_info), content_type='application/json')


def leaderboard(request):
    if request.method == "GET":
        high_score = Score.objects.all().order_by('-score')
        data = {'high_score': high_score}
        return render(request, 'leaderboard.html', data)