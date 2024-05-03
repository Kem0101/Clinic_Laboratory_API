from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Patient, Medical, Laboratorytest, Testorder, Orderdetail
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict

# Create your views here.


class PatientView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, patient_id=0):
        if (patient_id > 0):
            patients = list(Patient.objects.filter(
                patient_id=patient_id).values())
            if len(patients) > 0:
                patient = patients[0]
                data = {'message': "Success", 'patient': patient}
            else:
                data = {'message': "Patient not found..."}
            return JsonResponse(data)

        else:
            patients = list(Patient.objects.values())
            if len(patients) > 0:
                data = {'message': "Success", 'patients': patients}

            else:
                data = {'message': "Patients no found..."}

            return JsonResponse(data)

    def post(self, request):
        jdata = json.loads(request.body)
        Patient.objects.create(name=jdata['name'], lastname=jdata['lastname'], birth_date=jdata['birth_date'], gender=jdata['gender'],
                               address=jdata['address'], phone=jdata['phone'], email=jdata['phone'], id_card=jdata['id_card'])

        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, patient_id):
        jdata = json.loads(request.body)

        try:
            patient = Patient.objects.get(patient_id=patient_id)
            patient.name = jdata['name']
            patient.lastname = jdata['lastname']
            patient.birth_date = jdata['birth_date']
            patient.gender = jdata['gender']
            patient.address = jdata['address']
            patient.phone = jdata['phone']
            patient.email = jdata['email']
            patient.id_card = jdata['id_card']
            patient.save()
            data = {'message': "Success"}
        except Patient.DoesNotExist:
            data = {'message': "Patients no found..."}

        return JsonResponse(data)

    def delete(self, request, patient_id):

        try:
            patient = Patient.objects.get(patient_id=patient_id).delete()
            data = {'message': "Success"}

        except Patient.DoesNotExist:
            data = {'message': "Patients no found..."}

        return JsonResponse(data)


class MedicalView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, medical_id=0):
        if medical_id > 0:
            try:
                medical = Medical.objects.get(medical_id=medical_id)
                data = {'message': "Success",
                        'patient': model_to_dict(medical)}

            except Medical.DoesNotExist:
                data = {'message': "Patient not found..."}
        else:
            medicals = Medical.objects.all()
            if medicals.exists():
                data = {'message': "Success",
                        'Medicals': list(medicals.values())}
            else:
                data = {'message': "Medicals not found..."}

        return JsonResponse(data)


class LaboratoryTestView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, test_id=0):
        if test_id > 0:
            try:
                laboratorytest = Laboratorytest.objects.get(test_id=test_id)
                data = {'message': 'Success',
                        'laboratory test': model_to_dict(laboratorytest)}

            except Laboratorytest.DoesNotExist:
                data = {'message': 'Laboratory test not found'}

        else:
            laboratorytests = Laboratorytest.objects.all()
            if laboratorytests.exists():
                data = {'message': 'Success', 'Laboratory tests': list(
                    laboratorytests.values())}

            else:
                data = {'message': 'Laboratory tests not found'}

        return JsonResponse(data)


class TestOrderView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, order_id=0):
        if order_id > 0:
            try:
                testorder = Testorder.objects.get(order_id=order_id)
                data = {'message': 'Success',
                        'Test order': model_to_dict(testorder)}

            except Testorder.DoesNotExist:
                data = {'message': 'Test order not found'}

        else:
            testorders = Testorder.objects.all()
            if testorders.exists():
                data = {'message': 'Success',
                        'Test orders': list(testorders.values())}

            else:
                data = {'message': 'Test orders not found'}

        return JsonResponse(data)


class OrderDetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        try:
            ordersdetail = Orderdetail.objects.all()
            if ordersdetail.exists():
                data = {'message': 'Success',
                        'Orders': list(ordersdetail.values())}

            else:
                data = {'message': 'Orders detail not found'}

        except:
            print('Something was wrong')

        return JsonResponse(data)
