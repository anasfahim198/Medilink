from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'cnic', 'email', 'phone', 'doctor', 'booked_at')
    list_filter   = ('doctor__specialization',)
    search_fields = ('full_name', 'cnic', 'email')
    readonly_fields = ('booked_at',)
