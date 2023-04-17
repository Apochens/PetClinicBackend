# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from management.models import Department
from management.serializers import DepartmentSerializer


class DepartmentAPISingleViewTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(id=100, name='Test Department', description='Test Department Description')

    def test_get_department(self):
        url = reverse('department-api-single', args=[self.department.id])
        response = self.client.get(url)
        department = Department.objects.get(id=self.department.id)
        serializer = DepartmentSerializer(department)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['department'], serializer.data)

    def test_delete_department(self):
        url = reverse('department-api-single', args=[self.department.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Department.objects.filter(id=self.department.id).exists())