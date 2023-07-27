from django.urls import path
from . import views
app_name ='user_management'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('password_change/', views.password_change_view, name='password_change'),
    path('admin_password_change/', views.admin_password_change_view, name='admin_password_change'),
    path('set-security-question/', views.set_security_question, name='set_security_question'),

    # Other URL patterns...
]

