from django.db import models

class Perspective(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.category} (ID: {self.id})"

class PerspectiveTranslation(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('am', 'Amharic'),
        ('fr', 'French'),
    ]
    perspective = models.ForeignKey(
        Perspective, 
        on_delete=models.CASCADE, 
        related_name='translations'
    )
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        unique_together = ('perspective', 'language')

    def __str__(self):
        return f"{self.language.upper()}: {self.title}"