from django.urls import path
from .views import PatientView, MedicalView


urlpatterns = [
    path('patients/', PatientView.as_view(), name='patients_list'),
    path('patients/<int:patient_id>',
         PatientView.as_view(), name='patients_process'),
    path('medicals/', MedicalView.as_view(), name='medicals_list'),
    path('medicals/<int:medical_id>',
         MedicalView.as_view(), name='medicals_process')
]
