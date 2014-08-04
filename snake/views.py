from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from snake.forms import EmailUserCreationForm


def home(request):
    return render(request, 'base.html')


def snake(request):
    return render(request, 'snake.html')


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