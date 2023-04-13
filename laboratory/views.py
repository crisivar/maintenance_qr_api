from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import LaboratorySerializer
from .models import Laboratory
from django.contrib.auth.decorators import user_passes_test
from utils.my_utils import is_staff_or_superuser


class LaboratoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        laboratories = Laboratory.objects.all()
        serializer = LaboratorySerializer(laboratories, many=True)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def post(self, request):
        serializer = LaboratorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaboratoryDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Laboratory.objects.get(pk=pk)
        except Laboratory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        laboratory = self.get_object(pk)
        serializer = LaboratorySerializer(laboratory)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def put(self, request, pk):
        laboratory = self.get_object(pk)
        serializer = LaboratorySerializer(laboratory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @user_passes_test(is_staff_or_superuser)
    def delete(self, request, pk):
        laboratory = self.get_object(pk)
        laboratory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
