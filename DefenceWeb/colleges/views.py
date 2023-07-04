from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import api_view
from .models import College,News,Events,Partners,department,Univesity,Facilities,Office, Staffmember
from .serializers import CollageSerilizer,NewsSerilizer,EventsSerilizer,UniversitySerilizer,PartnerSerilizer,DepartmentSerilizer,FacilitySerilizer,OfficeSerilizer, StaffmemberSerilizer
from django.http import HttpResponse
from datetime import date
from django.db.models import Q

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
    current_date = date.today()
    queryset=Events.objects.filter(Q(date__gte=current_date))
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

class OfficeViewset(ReadOnlyModelViewSet):
    def get_queryset(self):
       
        return Office.objects.filter(college=self.kwargs['collage_pk'])
    
    serializer_class=OfficeSerilizer


class StaffmemberViewset(ReadOnlyModelViewSet):
    def get_queryset(self):
       
        return Staffmember.objects.all()
    
    serializer_class=StaffmemberSerilizer



