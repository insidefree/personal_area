from django.contrib import admin
from .models import Work


@admin.register(Work)
class AdminWork(admin.ModelAdmin):
    pass
