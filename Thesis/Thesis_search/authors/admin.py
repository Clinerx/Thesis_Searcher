from django.contrib import admin
from .models import Thesis


class ThesisAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'title', 'abstract')
# Register your models here.
admin.site.register(Thesis, ThesisAdmin)