from django.shortcuts import render

# Create your views here.
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import DepartmentsSerializer, JobsSerializer, HiredEmployeesSerializer
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        original_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print("time elapsed in ", func.__name__, ": ", end - start, sep='')
        return original_return_val

    return wrapper


class UploadAPIView(views.APIView):
    @timing_decorator
    def decode_csv(self, file_string, field_names):
        rows = []
        for row in file_string.split('\r\n'):
            fields = row.split(',')
            diction = {}
            for i in range(len(field_names)):
                diction[field_names[i]] = fields[i]
            rows.append(diction)
        return rows

    @timing_decorator
    def insert(self, serializer_class, rows):
        serializer = serializer_class(data=rows, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return True
        else:
            return False

    def execute(self, serializer_class, fields_names, file_uploaded):
        rows_in_dict = self.decode_csv(file_uploaded.read().decode(), fields_names)
        was_insertion_successful = self.insert(serializer_class, rows_in_dict)
        if was_insertion_successful:
            return Response("OK", status=status.HTTP_201_CREATED)
        else:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        file_uploaded = request.FILES.get('file')
        table_name = request.data["table"]
        if table_name == "hired_employees":
            response = self.execute(
                HiredEmployeesSerializer,
                ['id', 'name', 'datetime', 'department_id', 'job_id'],
                file_uploaded
            )
        elif table_name == "departments":
            response = self.execute(
                DepartmentsSerializer,
                ['id', 'department'],
                file_uploaded
            )
        elif table_name == "jobs":
            response = self.execute(
                JobsSerializer,
                ['id', 'job'],
                file_uploaded
            )
        else:
            response = table_name
        return response
