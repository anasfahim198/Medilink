from django.db import models
from doctors.models import Doctor


class Patient(models.Model):
    full_name   = models.CharField(max_length=100)
    cnic        = models.CharField(max_length=20)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20)
    disease     = models.TextField()
    doctor      = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='patients')
    booked_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-booked_at']

    def __str__(self):
        return f'{self.full_name} — {self.disease[:40]}'
