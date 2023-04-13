from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import EquipmentSerializer
from .models import Equipment
from django.contrib.auth.decorators import user_passes_test
from utils.my_utils import is_staff_or_superuser


class EquipmentList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipmentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        equipment = self.get_object(pk)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def put(self, request, pk):
        equipment = self.get_object(pk)
        serializer = EquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @user_passes_test(is_staff_or_superuser)
    def delete(self, request, pk):
        equipment = self.get_object(pk)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
