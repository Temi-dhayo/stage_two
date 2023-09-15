from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from stagetwo.models import Person
from stagetwo.serializers import PersonSerializer

# Create your views here.

class PersonCreateView(APIView):

    def post(self,request:HttpRequest)->Response:
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PersonDetailsView(APIView):

    def try_get_person(self, id)->Person|None:
        try:
            _id = int(id)
            try:
                person =  Person.objects.get(id=_id)
            except Person.DoesNotExist:
                return None
        except ValueError:
            try:
                person = Person.objects.get(name=id)
            except Person.DoesNotExist:
                return None
        return person
    
    def get(self,request:HttpRequest,id)->Response:
        person = self.try_get_person(id)
        if person is None:
            return Response({'error':'Person does not exist'},status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request:HttpRequest,id)->Response:
        person = self.try_get_person(id)
        if person is None:
            return Response({'error':'Person does not exist'},status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request:HttpRequest,id)->Response:
        person = self.try_get_person(id)
        if person is None:
            return Response({'error':'Person does not exist'},status=status.HTTP_404_NOT_FOUND)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)