from django.db import models

class CollegeName(models.Model):
    name = models.CharField(max_length = 70)
    leaderName = models.CharField(max_length = 70)
    welcomeMessage = models.TextField()
    about = models.TextField()
    departments = models.ForeignKey(to='self',on_delete=models.CASCADE)
    partners = models.ForeignKey(to='self', on_delete=models.CASCADE)

