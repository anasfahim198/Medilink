import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from doctors.models import Doctor
from .models import Patient


@csrf_exempt
@require_POST
def book_appointment(request):
    """
    Receives patient form data as JSON, saves to DB, returns confirmation.
    Called via fetch() in main.js when the user confirms an appointment.
    """
    try:
        data      = json.loads(request.body)
        full_name = data.get('name', '').strip()
        cnic      = data.get('cnic', '').strip()
        email     = data.get('email', '').strip()
        phone     = data.get('phone', '').strip()
        disease   = data.get('disease', '').strip()
        doctor_id = data.get('doctor_id')

        if not all([full_name, cnic, email, phone, disease]):
            return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)

        doctor = None
        if doctor_id:
            try:
                doctor = Doctor.objects.get(id=doctor_id)
            except Doctor.DoesNotExist:
                pass

        Patient.objects.create(
            full_name=full_name,
            cnic=cnic,
            email=email,
            phone=phone,
            disease=disease,
            doctor=doctor,
        )

        return JsonResponse({
            'success': True,
            'message': f'Appointment confirmed with {doctor.name if doctor else "a doctor"}.',
        })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
