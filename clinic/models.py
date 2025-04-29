from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=100)
    Mobile = models.IntegerField()
    Email = models.EmailField(max_length=100)
    Specialization = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class meta:
        ordering = ['-created_at'] 
   
class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Male', ('Male')
        FEMALE = 'Female', ('Female')
        
        OTHER = 'Other', ('Other')
        
        
    Name = models.CharField(max_length=100)
    Mobile = models.IntegerField(null=True, blank=True)
    
    gender= models.CharField(
        max_length=10,
        choices=Gender.choices,
        default=Gender.OTHER,
        blank=True, # Important: Allows form submission without selecting if default is not desired/sufficient
        verbose_name=("Gender")
    )
    Age = models.PositiveIntegerField(
        null=True,         # Allows the database column to store NULL
        blank=True,        # Allows the field to be blank in forms (validation)
        
    )
    Address = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class meta:
        ordering = ['-created_at'] # to show the latest added patient first
    
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Reason(models.Model):
    reason = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.reason   
    
class UserAppointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    dob= models.DateField()
    reason= models.ForeignKey(Reason, on_delete=models.CASCADE)
    details = models.TextField()
    appoint_date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True )
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.appoint_date) + ' ' + str(self.time) + ' ' + self.doctor.Name  