from django.urls import path
from .views import PatientView, MedicalView, LaboratoryTestView


urlpatterns = [
    path('patients/', PatientView.as_view(), name='patients_list'),
    path('patients/<int:patient_id>',
         PatientView.as_view(), name='patients_process'),

    path('medicals/', MedicalView.as_view(), name='medicals_list'),
    path('medicals/<int:medical_id>',
         MedicalView.as_view(), name='medicals_process'),

    path('laboratory-tests/', LaboratoryTestView.as_view(),
         name='laboratory_tests_list'),
    path('laboratory-tests/<int:test_id>',
         LaboratoryTestView.as_view(), name='laboratory_tests_list_process')
]
