from .models import Profile
from django.shortcuts import render
from .serializers import ProfileSLR
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

class ProfileView(GenericAPIView):
    serializer_class = ProfileSLR

    def get(self, request, format=None):
        candidate = Profile.objects.all()
        slr = self.serializer_class(candidate, many=True)
        return Response({'Msg':'Show all data', 'Candidates':f'{slr.data}'}, status=HTTP_200_OK)

    def post(self, request, format=None):
        slr = self.serializer_class(data=request.data)
        slr.is_valid(raise_exception=True)
        slr.save()
        return Response({'Msg':'Upload Successfully', 'Data':f'{slr.data}'}, status=HTTP_201_CREATED)