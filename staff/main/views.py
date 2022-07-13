from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Staff
from .serializers import StaffSerializer

def index(request):
    return render(request, 'main/index.html')


class StaffView(APIView):

    def get(self, request):
        staff_list = Staff.objects.all()
        serializer = StaffSerializer(staff_list, many=True)
        return Response({"staff_list": serializer.data})

    def post(self, request):
        staff = request.data.get('staff_list')

        serializer = StaffSerializer(data=staff)
        if serializer.is_valid(raise_exception=True):
            staff_saved = serializer.save()
        return Response({"success": "Staff '{}' created successfully".format(staff_saved.title)})

    def put(self, request, pk):
        saved_staff = get_object_or_404(Staff.objects.all(), pk=pk)
        data = request.data.get('staff_list')
        serializer = StaffSerializer(instance=saved_staff, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            staff_saved = serializer.save()
        return Response({
            "success": "Staff '{}' updated successfully".format(staff_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        staff = get_object_or_404(Staff.objects.all(), pk=pk)
        staff.delete()
        return Response({
            "message": "Staff with id `{}` has been deleted.".format(pk)
        }, status=204)
