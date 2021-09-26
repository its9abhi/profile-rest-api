from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloApiView (APIView):

    serializer_class=serializers.HelloSerializers



    def get(self,request,format=None):
        an_apiview=[
            'Uses HTTP method '
            'Is similer to Django'
            'Hey '
            'How are you'
        ]
        return Response({'message':'Hello !','an_apiview':an_apiview})

    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        """Handle Updating of Object"""
        return Response({'method':'Put'})

    def patch(self,request,pk=None):
        """Handle partial Upadating of Object"""
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        """Delete an Object"""
        return Response({'Method','DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_class=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
