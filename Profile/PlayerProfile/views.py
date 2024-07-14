from django.shortcuts import render
from django.http import HttpRequest,HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile, ScoreStats
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core import serializers


# Create your views here.

# class ProfileViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (JWTAuthentication)
#
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

class ProfileViewSet(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin, viewsets.mixins.ListModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)



class ScoreViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin,viewsets.mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Profile.objects.all()

    def list(self,request):
        user_id = request.user.id

        data = Profile.objects.filter(user=user_id).first()
        score = ScoreStats.objects.filter(user_hash=data.id_hash).first()

        name = data.name
        score = score.score

        jsonData = {
            'name':name,
            'score':score
        }

        return JsonResponse(jsonData)

    def create(self,request):

        user_id = request.user.id
        score = request.data.get('score')

        hash = Profile.objects.filter(user= user_id).first().id_hash
        scoreEntry = ScoreStats.objects.filter(user_hash=hash)

        jsonData = {}
        if (len(scoreEntry) !=0 ):
            jsonData = {
                'message': 'Sorry the user already exist'
            }
        else:
            s = ScoreStats.objects.create(user_hash=hash,score=score)
            s.save()
            jsonData ={
                'message' : 'Successfully added entry'
            }


        return JsonResponse(jsonData)









