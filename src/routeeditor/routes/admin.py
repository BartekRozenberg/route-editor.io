from django.contrib import admin
from .models import Route, Point

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'background_image', 'created_at')
    search_fields = ('name', 'user__username')

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('route', 'x', 'y', 'created_at')
    list_filter = ('route',)