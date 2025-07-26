from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('appoinments/', views.appointments_view, name='appointments'),
    path('approved/', views.approved_view, name='approved'),
    path('rejected/', views.rejected_view, name='rejected'),
    path('rescheduled/', views.rescheduled_view, name='rescheduled'),

    path('approve/<int:visitor_id>/', views.approve_visitor, name='approve_visitor'),
    path('reject/<int:visitor_id>/', views.reject_visitor, name='reject_visitor'),
    path('reschedule/<int:visitor_id>/', views.reschedule_form, name='reschedule_form'),
]
