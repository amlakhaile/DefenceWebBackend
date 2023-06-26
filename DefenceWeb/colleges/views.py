from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import api_view
from .models import College,News,Events,Partners,department,Univesity,Facilities
from .serializers import CollageSerilizer,NewsSerilizer,EventsSerilizer,UniversitySerilizer,PartnerSerilizer,DepartmentSerilizer,FacilitySerilizer
from django.http import HttpResponse

class Collageviewset(ReadOnlyModelViewSet):
    queryset=College.objects.all()
    serializer_class=CollageSerilizer
class Universityviewset(ReadOnlyModelViewSet):
    queryset=Univesity.objects.all()
    serializer_class=UniversitySerilizer
class Newsviewset(ReadOnlyModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerilizer
class Eventsviewset(ReadOnlyModelViewSet):
    queryset=Events.objects.all()
    serializer_class=EventsSerilizer
class PartnerViewset(ReadOnlyModelViewSet):
    def get_queryset(self):
       
        return Partners.objects.filter(college=self.kwargs['collage_pk'])
    
    serializer_class=PartnerSerilizer
class DepartmentViewset(ReadOnlyModelViewSet):
    def get_queryset(self):
       
        return department.objects.filter(college=self.kwargs['collage_pk'])
    
    serializer_class=DepartmentSerilizer
class FacilitiesViewset(ReadOnlyModelViewSet):
    def get_queryset(self):
       
        return Facilities.objects.filter(collage=self.kwargs['collage_pk'])
    
    serializer_class=FacilitySerilizer
