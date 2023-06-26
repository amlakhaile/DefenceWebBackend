from rest_framework import serializers
from .models import College,News,Events,department,Partners,HelpTexts,Univesity,Facilities
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
        fields=['id','name','photo','college']
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