from django import forms
from .models import Habit, Category, HabitRecord, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import PasswordInput, TextInput

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency', 'target_count', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(HabitForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(
                user__in=[user, None]
            ).distinct()
        else:
            self.fields['category'].queryset = Category.objects.all()


class HabitRecordForm(forms.ModelForm):
    class Meta:
        model = HabitRecord
        fields = ['completed', 'completed_count', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
    }
        

class loginform(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    

class registerForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']