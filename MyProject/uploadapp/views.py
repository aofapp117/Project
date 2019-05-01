from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import File

from .serializers import FileSerializer
from django.core import serializers
from django.http import HttpResponse

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUpdateView(APIView):
    def post(self, request,number, *args, **kwargs):
        data=request.data
        print(data)
        q=File.objects.get(pk=number)
        q.like+=1
        q.save()


# class FileloadView(APIView):
#     def get(self, request, *args, **kwargs):
#         file_list=File.objects.all
#         file_serializer = FileSerializer
#         return Response([{
#     'username': 'lizzy',
#      'email': 'lizzy@example.com',
#     'profile': {'address': '123 Acacia Avenue', 'phone': '01273 100200'}} ,
#     {
#     'username': 'lizzy',
#      'email': 'lizzy@example.com',
#     'profile': {'address': '123 Acacia Avenue', 'phone': '01273 100200'}}])


class FileloadView(APIView):
    def get(request, *args, **kwargs):
        queryset=File.objects.order_by('-pk')
        queryset = serializers.serialize('json',queryset)
        return HttpResponse(queryset, content_type='application/json')

def like(request,number):
        q=File.objects.get(pk=number)
        q.like+=1
        q.save()
