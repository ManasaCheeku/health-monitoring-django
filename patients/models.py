from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    symptoms = models.TextField()
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate QR code before saving
        url = f"http://localhost:8000/patients/patient/{self.user.id}/"
        qr = qrcode.make(url)
        blob = BytesIO()
        qr.save(blob, 'PNG')
        self.qr_code.save(f'qr_{self.user.id}.png', File(blob), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
