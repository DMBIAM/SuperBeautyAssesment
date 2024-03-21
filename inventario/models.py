from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    """
    Represents an equipment item in the inventory.

    Each equipment item has a reference, brand, processor, memory,
    disk, and type. These attributes define the specifications
    and characteristics of the equipment.
    """
    reference = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    disk = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the equipment item.

        Returns the reference of the equipment as its string representation.
        """
        return self.reference

class EquipmentUser(models.Model):
    """
    Represents the assignment of an equipment item to a user.

    Each equipment user instance links an equipment item to a user,
    indicating the assignment date and delivery date of the equipment.
    """
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment_date = models.DateField()
    delivery_date = models.DateField()

    def __str__(self):
        """
        Returns a string representation of the equipment assignment.

        Returns a string containing the reference of the assigned equipment
        and the username of the user it is assigned to.
        """
        return f"{self.equipment.reference} assigned to {self.user.username}"
