from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Patient

class PatientAppTests(TestCase):

    def setUp(self):
        # Create a test user and patient record
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.patient = Patient.objects.create(
            user=self.user,
            name='Initial Name',
            age=30,
            gender='Male',
            phone_number='1234567890',
            email='test@example.com',
            location='Test City',
            symptoms='Cough and fever'
        )
        self.client = Client()

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patients/register.html')

    def test_login_logout(self):
        login = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login)
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")

        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_edit_report(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('edit_report'), {
            'name': 'Updated Name',  # ✅ Added missing required field
            'age': 35,
            'gender': 'Male',
            'phone_number': '9876543210',
            'email': 'test@example.com',
            'location': 'New City',
            'symptoms': 'Headache',
        })
        self.assertRedirects(response, reverse('home'))
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.name, 'Updated Name')  # ✅ Assert name updated
        self.assertEqual(self.patient.age, 35)
        self.assertEqual(self.patient.gender, 'Male')
        self.assertEqual(self.patient.phone_number, '9876543210')
        self.assertEqual(self.patient.location, 'New City')
        self.assertEqual(self.patient.symptoms, 'Headache')

    def test_patient_detail_access(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('patient_detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cough and fever')

    def test_contact_page_get_and_post(self):
        # Test GET request
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patients/contact.html')

        # Test POST request
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Hello, this is a test message.',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your message has been sent successfully!')
