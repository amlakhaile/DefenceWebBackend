from typing import Any, Dict, Iterable, Optional, Tuple
from django.db import models

class College(models.Model):
    name = models.CharField(max_length = 70)
    leaderName = models.CharField(max_length = 70)
    welcomeMessage = models.TextField()
    about = models.TextField()
    adminstartion=models.TextField()
    leaderimage=models.ImageField(upload_to='leader' ,blank=True)
    
    
    pathname=models.CharField(max_length=10)
    bannerimage=models.ImageField(upload_to='collage')
    def __str__(self):
        return self.name

class Univesity(models.Model):
   
    leaderName = models.CharField(max_length = 70)
    leaderimage=models.ImageField(upload_to='leader',blank=True)
    welcomeMessage = models.TextField()
    about = models.TextField()
    adminstartion=models.TextField()
    
    
    pathname=models.CharField(max_length=10)
    bannerimage=models.ImageField(upload_to='collage')
    def __str__(self):
        return self.pathname

class department(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='collage')
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    background = models.TextField(null=True, blank=True)
    historyofdepartment = models.TextField(null=True, blank=True)
    scope = models.TextField(null = True, blank=True)
    academicgoals = models.TextField(null = True, blank=True)
    academicprogram = models.TextField(null = True, blank=True)
    admissionrequirement = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    officephone = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Departmentfacilities(models.Model):
    name = models.CharField(max_length = 255, null=True, blank=True)
    image = models.ImageField(upload_to='collage', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Partners(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='collage')
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class HelpTexts(models.Model):
    title=models.CharField(max_length=70)
    description=models.TextField()
    def __str__(self):
        return self.title


class Events(models.Model):
    Title=models.CharField(max_length=70)
    description=models.TextField()
    date=models.DateField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.Title


class News(models.Model):
    News_type = (
        ('Announcment', 'Announcment'),
        ('Research', 'Research'),
        ('News', 'News'),
    )
    Title=models.CharField(max_length=70)
    type= models.CharField(max_length=13, choices=News_type,default="News")
    image=models.ImageField(upload_to='news',null=True)
    description=models.TextField()
    date=models.DateField(auto_now_add=True)
    tags=models.ManyToManyField(College)
    def __str__(self):
        return self.Title

class CommunityOutreach(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
class Facilities(models.Model):
    Facilityname=models.CharField(max_length=70)
    Facilities_detail=models.TextField()
    image=models.ImageField(upload_to='facilities',null=True)
    collage=models.ForeignKey(College,on_delete=models.CASCADE)
    def __str__(self):
        return self.Facilityname


class Staffmember(models.Model):
    name = models.CharField(max_length=255)
    academicRank = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    startingDate = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    educationAttended = models.TextField(blank=True)
    email = models.EmailField(max_length = 255, blank=True)
    contact_number = models.CharField(max_length = 14, blank=True)
    leader_role = models.CharField(max_length = 30, blank=True)
    image = models.ImageField(upload_to='leader', null=True)
    facebooklink = models.CharField(max_length=255, null=True)
    biography = models.TextField(null=True)
    linkedin = models.CharField(max_length = 255, null=True)
    researchInterest = models.TextField(null=True)
    

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='facilities', null=True)

    def __str__(self):
        return self.name

class Office(models.Model):
    OFFICE_CHOICES = (
        ('Commandant Office', 'Commandant Office'),
        ('Foreign Relation Office', 'Foreign Relation Office'),
        ('Academic Office', 'Academic Office'),
        ('Quality Assurance Office', 'Quality Assurance Office'),
        ('Post Graduation Office', 'Post Graduation Office'),
        ('Registrar Office', 'Registrar Office'),
        ('Logistics and Housing Office', 'Logistics and Housing Office'),
        ('Law Office', 'Law Office'),
        ('Student Council Office', 'Student Council Office'),
        ('Office of Human Resource', 'Office of Human Resource'),
        ('Office of Security', 'Office of Security')
    )
    name = models.CharField(max_length=30, choices=OFFICE_CHOICES, default='Academic Office')
    email = models.EmailField(max_length=255)
    contact_number = models.CharField(max_length=14)
    leaderuser = models.ForeignKey(Staffmember, on_delete=models.CASCADE, related_name='leaders')
    staffmembers = models.ManyToManyField(Staffmember, related_name='members')
    about = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'college')

    def __str__(self):
        return str(self.college)+" "+self.name
    


        
class Programs(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    photo=models.ImageField(upload_to='collage', null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
   


