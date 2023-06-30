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
class Univesity(models.Model):
   
    leaderName = models.CharField(max_length = 70)
    leaderimage=models.ImageField(upload_to='leader',blank=True)
    welcomeMessage = models.TextField()
    about = models.TextField()
    adminstartion=models.TextField()
    
    
    pathname=models.CharField(max_length=10)
    bannerimage=models.ImageField(upload_to='collage')
class department(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='collage')
    college = models.ForeignKey(College,on_delete=models.CASCADE)
class Partners(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='collage')
    college = models.ForeignKey(College, on_delete=models.CASCADE)

class HelpTexts(models.Model):
    title=models.CharField(max_length=70)
    description=models.TextField()

class Events(models.Model):
    Title=models.CharField(max_length=70)
    description=models.TextField()
    date=models.DateField()
    location=models.CharField(max_length=100)

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
class CommunityOutreach(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
class Facilities(models.Model):
    Facilityname=models.CharField(max_length=70)
    Facilities_detail=models.TextField()
    image=models.ImageField(upload_to='facilities',null=True)
    collage=models.ForeignKey(College,on_delete=models.CASCADE)








