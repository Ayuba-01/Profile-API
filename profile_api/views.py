from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from .serializers import HelloSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile, ProfileFeedItem
from .permission import IsOwnerOrAuthenticatedReadOnly, UpdateOwnStatus




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
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "email"]
    
    
class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES 
    

class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnStatus, IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)