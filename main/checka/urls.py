from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('habits/', views.habit_list_create, name='habit_list_create'),
    path('habits/<int:pk>', views.habit_update, name='habit_update'),
    path('categorycreate/', views.category_create, name='category_create'),
    path('habitrecord/<int:pk>', views.habit_record_create, name='habit_record'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('records/', views.habit_record_list, name='records'),
    path('records/<int:pk>', views.habit_record_edit, name='records_update'),
    path('records/<int:pk>/delete', views.habit_record_delete, name='records_delete'),
    path('', views.landing_page, name='landing_page'),
]