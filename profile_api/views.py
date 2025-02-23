from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer, UserProfileSerializer
from rest_framework import viewsets
from .models import UserProfile
from .permission import IsOwnerOrAuthenticatedReadOnly
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    
    serializer_class = HelloSerializer
    def get(self, request, format=None):
        
        an_apiview = [
            "Hello", "Hi", "Hey",
        ]
        
        return Response({'message': 'greetings', 'an_apiview':an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        name = serializer.validated_data.get("name")
        return Response({"message": f"Hello {name}" })
    
    def put (self, request, pk=None):
        return 
    
    
class HelloViewSet(viewsets.ViewSet):
    serializer_class = HelloSerializer
    
    def list(self, request):
        a_viewset = [
            "Helloooo", "Hiii", "Heyyyy",
        ]
        
        return Response({"message":"Hello", "a_viewset":a_viewset})
    
    def create(self, reqeust):
        serializer = self.serializer_class(data=reqeust.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return Response({"message":f"Hello {name}"})
    
    

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsOwnerOrAuthenticatedReadOnly]
    authentication_classes = [TokenAuthentication]