from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from routes.models import Route, Point
from users.models import BackgroundImage

@login_required
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        background_id = request.POST.get('background_image')
        background_image = get_object_or_404(BackgroundImage, id=background_id)
        Route.objects.create(name=name, user=request.user, background_image=background_image)
        return redirect('home')

    routes = Route.objects.filter(user=request.user)
    backgrounds = BackgroundImage.objects.all()
    return render(request, 'home.html', {'routes': routes, 'backgrounds': backgrounds})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto dla użytkownika {username} zostało utworzone! Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})