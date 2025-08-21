from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """
    Optional: Group habits into categories (e.g., Health, Productivity).
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['user', 'name'] # Ensure unique category names per user

    def __str__(self):
        return self.name


class Habit(models.Model):
    """
    Represents a habit to be tracked.
    """
    FREQUENCY_CHOICES = (
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='habits')
    is_active = models.BooleanField(default=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='DAILY')
    target_count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_frequency_display()})"
    
    def get_absolute_url(self):
        return reverse(
            'checka:habit_update', args=[self]
            )


class HabitRecord(models.Model):
    """
    Tracks each completion of a habit.
    """
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='records')
    date = models.DateField(default=date.today)
    completed = models.BooleanField(default=False)
    completed_count = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['habit', 'date']

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.completed else 'Incomplete'}"
    
    def get_absolute_url(self):
        return reverse(
            'checka:records_update', args=[self]
            )
