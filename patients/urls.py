from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('edit_report/', views.edit_report, name='edit_report'),
    path('patient/<int:user_id>/', views.patient_detail, name='patient_detail'),
    path('contact/', views.contact, name='contact'),
    path('api/patient/', views.patient_api, name='patient_api'),
    path('chatbot/', views.chatbot, name='chatbot'),  # 👈 chatbot dummy view
]
