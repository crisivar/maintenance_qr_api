from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Activity
from .serializers import ActivitySerializer
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test
from utils.my_utils import is_staff_or_superuser


class ActivityList(APIView):
    permission_classes = [IsAuthenticated]
    """
    Lista todas las actividades o crea una nueva.
    """

    def get(self, request, format=None):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def post(self, request, format=None):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    Recupera, actualiza o elimina una actividad existente.
    """

    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    @user_passes_test(is_staff_or_superuser)
    def put(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @user_passes_test(is_staff_or_superuser)
    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
