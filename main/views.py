from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.response import Response
from .serializers import JournalSerializer, RegisterSerializer, UserSerializer, WashCompanySerializer
from django.forms import model_to_dict
from .models import Journal, User, WashCompany
#Register API
from django.contrib.auth.hashers import make_password

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })



class JournalAPIView(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    


class WashCompanyCreateApi(generics.GenericAPIView):
    serializer_class = WashCompanySerializer
    
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        washCompany = serializer.save()
        return Response({
            "washCompany": WashCompanySerializer(washCompany, context=self.get_serializer_context()).data,
            
            "message": "Wash Company Created Successfully.",
        })




class GetCompany(generics.GenericAPIView):
        
    def post(self, request, *args, **kwargs):
        
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.get(username=username)
            print(user)
            return Response({'company_id': user.washCompany.id, 'company_name': user.washCompany.name})
        except:
            return Response({'error': 'username or password error'})
            

# class LogOut