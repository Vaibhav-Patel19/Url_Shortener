from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import url
from .serializers import ReactSerializer



@api_view(['GET', 'POST'])
def urlList(request):
    if(request.method == 'GET'):
        urls = url.objects.all()
        serializer = ReactSerializer(urls, many = True)
        return Response(serializer.data)
    elif(request.method == 'POST'):
        serializer = ReactSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)