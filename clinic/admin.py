from django.contrib import admin
from .models import Doctor, Patient, Appointment, Reason, UserAppointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Reason)
admin.site.register(UserAppointment)
