import json
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from .models import Equipment, EquipmentUser

class EquipmentModelTestCase(TestCase):
    """
    Test case for the Equipment model.

    Sets up a test instance of the Equipment model and verifies
    that the fields are correctly saved and retrieved.
    """
    def setUp(self):
        """
        Set up a test instance of the Equipment model.
        """
        self.equipment = Equipment.objects.create(
            reference='Test Reference',
            brand='Test Brand',
            processor='Test Processor',
            memory='Test Memory',
            disk='Test Disk',
            type='Test Type'
        )

    def test_equipment_fields(self):
        """
        Test the fields of the Equipment model.
        """
        equipment = Equipment.objects.get(reference='Test Reference')
        self.assertEqual(equipment.reference, 'Test Reference')
        self.assertEqual(equipment.brand, 'Test Brand')
        self.assertEqual(equipment.type, 'Test Type')

class EquipmentUserModelTestCase(TestCase):
    """
    Test case for the EquipmentUser model.

    Sets up a test instance of the EquipmentUser model and verifies
    that the fields are correctly saved and retrieved.
    """
    def setUp(self):
        """
        Set up a test instance of the EquipmentUser model.
        """
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.equipment = Equipment.objects.create(
            reference='Test Reference',
            brand='Test Brand',
            processor='Test Processor',
            memory='Test Memory',
            disk='Test Disk',
            type='Test Type'
        )
        self.equipment_user = EquipmentUser.objects.create(
            equipment=self.equipment,
            user=self.user,
            assignment_date='2024-03-25',
            delivery_date='2024-04-01'
        )

    def test_equipment_user_fields(self):
        """
        Test the fields of the EquipmentUser model.
        """
        equipment_user = EquipmentUser.objects.get(user=self.user)
        self.assertEqual(equipment_user.equipment.reference, 'Test Reference')
        self.assertEqual(equipment_user.user.username, 'testuser')
        self.assertEqual(equipment_user.assignment_date.isoformat(), '2024-03-25')

class EquipmentListViewTestCase(APITestCase):
    """
    Test case for the EquipmentListView API view.

    Tests the retrieval of equipment data via GET request.
    """
    def setUp(self):
        """
        Set up a test instance of the Equipment model and the URL.
        """
        self.equipment = Equipment.objects.create(
            reference='Test Reference',
            brand='Test Brand',
            processor='Test Processor',
            memory='Test Memory',
            disk='Test Disk',
            type='Test Type'
        )
        self.url = reverse('equipment-list')

    def test_get(self):
        """
        Test the GET request to retrieve equipment data.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data[0]['reference'], 'Test Reference')
        self.assertEqual(data[0]['brand'], 'Test Brand')
        self.assertEqual(data[0]['type'], 'Test Type')