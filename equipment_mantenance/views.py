from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EquipmentMaintenance
from .serializers import EquipmentMaintenanceSerializer


class EquipmentMaintenanceList(APIView):
    """
    Lista todas las actividades de mantenimiento de equipos, o crea una nueva.
    """

    def get(self, request, format=None):
        equipment_maintenances = EquipmentMaintenance.objects.all()
        serializer = EquipmentMaintenanceSerializer(
            equipment_maintenances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EquipmentMaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipmentMaintenanceDetail(APIView):
    """
    Recupera, actualiza o elimina una actividad de mantenimiento de
    equipos existente.
    """

    def get_object(self, pk):
        try:
            return EquipmentMaintenance.objects.get(pk=pk)
        except EquipmentMaintenance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        equipment_maintenance = self.get_object(pk)
        serializer = EquipmentMaintenanceSerializer(equipment_maintenance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        equipment_maintenance = self.get_object(pk)
        serializer = EquipmentMaintenanceSerializer(
            equipment_maintenance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        equipment_maintenance = self.get_object(pk)
        equipment_maintenance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
