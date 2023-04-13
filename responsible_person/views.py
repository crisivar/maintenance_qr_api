from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ResponsiblePerson
from .serializers import ResponsiblePersonSerializer
from django.contrib.auth.decorators import user_passes_test
from utils.my_utils import is_staff_or_superuser


class ResponsiblePersonList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        persons = ResponsiblePerson.objects.all()
        serializer = ResponsiblePersonSerializer(persons, many=True)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def post(self, request):
        serializer = ResponsiblePersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponsiblePersonDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ResponsiblePerson.objects.get(pk=pk)
        except ResponsiblePerson.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = ResponsiblePersonSerializer(person)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def put(self, request, pk):
        person = self.get_object(pk)
        serializer = ResponsiblePersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @user_passes_test(is_staff_or_superuser)
    def delete(self, request, pk):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
