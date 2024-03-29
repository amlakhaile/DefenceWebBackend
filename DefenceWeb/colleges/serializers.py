from rest_framework import serializers
from .models import College,News,Events,department,Partners,HelpTexts,Univesity,Facilities, Office, Staffmember, Gallery, Departmentfacilities, Programs
from django.shortcuts import get_object_or_404
class CollageSerilizer(serializers.ModelSerializer):
    class Meta:
        model=College
        fields=['id','name','leaderName','welcomeMessage','leaderimage','about','adminstartion','pathname','bannerimage']
class UniversitySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Univesity
        fields=['id','leaderName','welcomeMessage','leaderimage','about','adminstartion','pathname','bannerimage']
class DepartmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=department
        fields=['id','name','photo','college','background', 'historyofdepartment', 'scope', 'academicgoals','academicprogram', 'admissionrequirement', 'email', 'officephone', 'fax']
class PartnerSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Partners
        fields=['id','name','photo','college']
class NewsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','Title','type','image','description','date','tags']
class EventsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=['id','Title','description','date','location']
class HelptSerilizer(serializers.ModelSerializer):
    class Meta:
        model=HelpTexts
        fields=['id','Title','description']
class FacilitySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Facilities
        fields=['id','Facilityname','Facilities_detail','image','collage']

class OfficeSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Office
        fields=['id','name','email','contact_number', 'about','leaderuser','staffmembers']

class StaffmemberSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Staffmember
        fields=['id','name','academicRank','department','startingDate','educationAttended','email','contact_number','leader_role','image','facebooklink', 'biography', 'linkedin', 'researchInterest', 'college']

class GallerySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields=['id','name','image']

class DepartmentfacilitiesSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Departmentfacilities
        fields=['id','name','image', 'about', 'department']

class ProgramsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Programs
        fields=['id','name','photo', 'college']