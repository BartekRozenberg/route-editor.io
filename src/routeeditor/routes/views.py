from django.shortcuts import render, redirect, get_object_or_404
from .models import Route, Point
from users.models import BackgroundImage
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import JsonResponse

@login_required
def create_route(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        background_id = request.POST.get('background_image')
        background_image = get_object_or_404(BackgroundImage, id=background_id)
        route = Route.objects.create(name=name, user=request.user, background_image=background_image)
        return redirect('route_list')
    backgrounds = BackgroundImage.objects.all()
    return render(request, 'routes/create_route.html', {'backgrounds': backgrounds})

@login_required
def route_list(request):
    routes = Route.objects.filter(user=request.user)
    return render(request, 'routes/route_list.html', {'routes': routes})

@login_required
def edit_route(request, route_id):
    route = get_object_or_404(Route, id=route_id, user=request.user)
    if request.method == 'POST':
        x = request.POST.get('x')
        y = request.POST.get('y')
        if x and y:
            Point.objects.create(route=route, x=float(x), y=float(y))
        return redirect('edit_route', route_id=route.id)

    points = list(route.points.values('x', 'y'))
    return render(request, 'routes/edit_route.html', {'route': route, 'points': points})