from django.db import models

class BackgroundImage(models.Model):
    name = models.CharField(max_length=100, help_text="Nazwa obrazu tła")
    image = models.ImageField(upload_to='media/backgrounds/', help_text="Plik obrazu tła")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name