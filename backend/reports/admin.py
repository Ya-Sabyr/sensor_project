from django.contrib import admin
from .models import Record
# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    model = Record
    

admin.site.register(Record, RecordAdmin)