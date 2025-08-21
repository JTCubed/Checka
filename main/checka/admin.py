from django.contrib import admin
from .models import HabitRecord, Habit, Category
# Register your models here.


admin.site.register(Category)
admin.site.register(Habit)
admin.site.register(HabitRecord)
