from rest_framework import serializers
from .models import Departments, Jobs, HiredEmployees


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['id', 'job', ]


class HiredEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiredEmployees
        fields = ['id', 'name', 'datetime', 'department_id', 'job_id', ]


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'department', ]


class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    table = serializers.CharField()

    class Meta:
        fields = ['file', 'table']
