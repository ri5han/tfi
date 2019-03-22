from django.db import models
#from user.models import Post
#from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    opportunity_title = models.CharField(max_length=50, null=True)
    opportunity_creator = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20)
    volunteer_email = models.EmailField()
    mobile = models.CharField(max_length=10)
    commitment_time = models.IntegerField(default=1)
    why_TFI = models.TextField(max_length=250)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name
