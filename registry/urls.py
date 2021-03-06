'''
URLs for registry app
'''

from django.urls import path
from . import views

urlpatterns = [
    path('clinics/', views.clinics, name='clinics'),
    path('clinic/add', views.clinic_add, name='clinic_add'),
    path('clinic/<int:id>', views.clinic, name='clinic'),
    path('clinic/<int:id>/update', views.clinic_update, name='clinic_update'),
    path('clinic/<int:id>/delete', views.clinic_delete, name='clinic_delete'),
    path('clinic/<int:id>/doctor/add', views.doctor_add, name='doctor_add'),
    path('clinic/<int:id>/logbook/add', views.logbook_add, name='logbook_add'),

    path('doctor/<int:id>', views.doctor, name='doctor'),
    path('doctor/<int:id>/update', views.doctor_update, name='doctor_update'),
    path('doctor/<int:id>/delete', views.doctor_delete, name='doctor_delete'),
    path('doctors/', views.doctors, name='doctors'),

    path('patients/', views.patients, name='patients'),
    path('patient/add', views.patient_add, name='patient_add'),
    path('patient/<int:id>', views.patient, name='patient'),
    path('patient/<int:id>/update', views.patient_update, name='patient_update'),
    path('patient/<int:id>/delete', views.patient_delete, name='patient_delete'),
    path('patient/<int:id>/print', views.patient_print, name='patient_print'),
    path('patient/<int:id>/immunization/add', views.immunization_add, name='immunization_add'),

    path('immunizations/', views.immunizations, name='immunizations'),
    path('immunization/<int:id>', views.immunization, name='immunization'),
    path('immunization/<int:id>/update', views.immunization_update, name='immunization_update'),
    path('immunization/<int:id>/delete', views.immunization_delete, name='immunization_delete'),
    path('immunization/<int:id>/print', views.immunization_print, name='immunization_print'),

    path('logbook/', views.logbook, name='logbook'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]







