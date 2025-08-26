from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Habit, Category, HabitRecord
from .forms import HabitForm, HabitRecordForm, CategoryCreateForm, loginform, registerForm
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime


@login_required(login_url=settings.LOGIN_URL)
def habit_list_create(request):
    # List habits for the user
    habits = Habit.objects.filter(user=request.user)
    usrnme = request.user.username
    #paginator = Paginator(habits, 10)  # Show 10 habits per page
    categories = Category.objects.filter(user__in=[request.user]).distinct()
    dcategories = Category.objects.filter(user=None).distinct()
    # stat =
    error_message = None

    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit_name = form.cleaned_data['name']
            if Habit.objects.filter(user=request.user, name=habit_name).exists():
                error_message = "You already have a habit with this name."
            else:
                habit = form.save(commit=False)
                habit.user = request.user
                habit.save()
                return redirect(reverse_lazy('habit_list_create'))
    else:
        form = HabitForm()

    context = {
        'object_list': habits,
        'form': form,
        'categories': categories,
        'dcategories': dcategories,
        'error_message': error_message,
        'username': usrnme,
    }
    return render(request, 'checka/habit_list.html', context)


@login_required(login_url=settings.LOGIN_URL)
def habit_update(request, pk):
    habit = Habit.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(reverse_lazy('habit_list_create'))
    else:
        form = HabitForm(instance=habit)

    context = {
        'form': form,
        'habit': habit,
    }
    return render(request, 'checka/habit_update.html', context)

@login_required(login_url=settings.LOGIN_URL)
def habit_record_create(request, pk):
    habit = Habit.objects.get(pk=pk, user=request.user)
    
    if request.method == "POST":
        form = HabitRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(reverse_lazy('habit_list_create'))
    else:
        form = HabitRecordForm()
    context = {'form': form, 'habit':habit}
    return render(request, 'checka/habitrecord.html', context)

@login_required(login_url=settings.LOGIN_URL)
def habit_record_list(request):
    habits = Habit.objects.filter(user=request.user).prefetch_related("records")
    
    for i in habits:
        print(i.name, i.records.all())
    
    context = {'habits':habits}
    return render(request, 'checka/habit_record_list.html', context)
    # trecords = HabitRecord.objects.filter( 
    #     user=request.user).order_by('-created_at')

@login_required(login_url=settings.LOGIN_URL)
def habit_record_edit(request, pk):
    record = HabitRecord.objects.get(id=pk)
    form = HabitRecordForm(instance=record)
    if request.method == 'POST':
        form = HabitRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("records")
    context = {"form": form, "record": record}

    return render(request, "checka/habit_record_update.html", context)

@login_required(login_url=settings.LOGIN_URL)
def habit_record_delete(request, pk):
    record = HabitRecord.objects.get(id=pk)
    record.delete()
    return redirect("records")

@login_required(login_url=settings.LOGIN_URL)
def category_create(request):
    categories = Category.objects.filter(user__in=[request.user]).distinct()
    dcategories = Category.objects.filter(user=None).distinct()
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect(reverse_lazy('habit_list_create'))
    else:
        form = CategoryCreateForm()
    context = {
        'form': form,
        'categories': categories,
        'dcategories': dcategories,
    }
    return render(request, 'checka/category_create.html', context)





def login_view(request):
    error_message = None
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, 
                                username=username, 
                                password=password
                                )
            if user is not None:
                login(request, user)
                return redirect('habit_list_create')
            else:
                error_message = "Invalid username or password."
        else:
            print(form.errors)
    else:
         form = loginform()
    context = {'form':form, 'error':error_message}
    return render(request, 'registration/login.html', context)


def register_view(request):
    error_message = None
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username,
                                            password=password)
            login(request, user)
            return redirect('habit_list_create')
        else:
            error_message = 'Passwords did not match'
    else:
        form = registerForm()

    context = {'form':form, 'error': error_message}
    return render(request, 'registration/register.html', context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('habit_list_create')



def landing_page(request):
    categories = Category.objects.filter(user=None)[:6]  # default categories
    return render(request, 'landing_page.html', {'categories': categories, 'year': datetime.now().year})