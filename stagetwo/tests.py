from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from stagetwo.models import Person
from stagetwo.serializers import PersonSerializer

# Create your tests here.

class PersonAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'name': 'John Doe',
        }
        # self.invalid_payload = {
        #     'name': '',
        # }
        self.person = Person.objects.create(name='Alice')

    def test_create_person(self):
        response = self.client.post('/api/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_create_invalid_person(self):
    #     response = self.client.post('/api/', self.invalid_payload, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_person(self):
        response = self.client.get(f'/api/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_person(self):
        response = self.client.get('/api/999/')  # Assuming this ID does not exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_person(self):
        updated_payload = {
            'name': 'Updated Name',
        }
        response = self.client.put(f'/api/{self.person.id}/', updated_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        response = self.client.delete(f'/api/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
