from django.db import models
from django.contrib.auth.models import User
from users.models import BackgroundImage

class Route(models.Model):
    name = models.CharField(max_length=100, help_text="Nazwa trasy")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routes")
    background_image = models.ForeignKey(BackgroundImage, on_delete=models.CASCADE, related_name="routes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Point(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="points")
    x = models.FloatField(help_text="Współrzędna X")
    y = models.FloatField(help_text="Współrzędna Y")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Point ({self.x}, {self.y}) on {self.route.name}"