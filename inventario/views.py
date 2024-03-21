from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Equipment

class EquipmentListView(APIView):
    """
    A view to retrieve a list of equipment via GET request.

    Retrieves all equipment instances from the database and returns
    a serialized representation containing reference, brand, and type
    information for each equipment item.
    """
    def get(self, request):
        """
        Handle GET request and return a list of equipment.

        Retrieves all equipment instances from the database and formats
        the data into a list of dictionaries, each containing reference,
        brand, and type information for an equipment item. Returns the
        serialized data as a JSON response.
        """
        equipment = Equipment.objects.all()
        data = [{'reference': item.reference, 'brand': item.brand, 'type': item.type} for item in equipment]
        return Response(data)
