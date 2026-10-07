from django.contrib import admin
from .models import Perspective, PerspectiveTranslation

# Register your models here.
class PerspectiveTranslationInline(admin.StackedInline):
    model=PerspectiveTranslation
    extra=1

@admin.register(Perspective)
class PerspectiveAdmin(admin.ModelAdmin):
    list_display=("id", "category", "created_at")
    inlines=[PerspectiveTranslationInline]

