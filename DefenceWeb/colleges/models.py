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
    leader = models.CharField(max_length = 30, blank=True)
    image = models.ImageField(upload_to='leader', null=True)

    def __str__(self):
        return self.name
class Office(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255)
    contact_number = models.CharField(max_length = 14)
    leaderuser=models.ForeignKey(Staffmember,on_delete=models.CASCADE ,related_name='leaders')
    staffmembers=models.ManyToManyField(Staffmember, related_name='members')
    
    about = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

