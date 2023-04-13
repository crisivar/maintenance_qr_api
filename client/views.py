from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .serializers import ClientSerializer
from django.contrib.auth.decorators import login_required, user_passes_test
from utils.my_utils import is_staff_or_superuser


class ClientList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = ClientSerializer(category)
        return Response(serializer.data)

    @login_required
    @user_passes_test(is_staff_or_superuser)
    def put(self, request, pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @user_passes_test(is_staff_or_superuser)
    def delete(self, request, pk):
        client = Client.objects.get(pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
