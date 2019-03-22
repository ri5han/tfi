from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    creator = models.CharField(max_length=10, null=True)
    creator_email = models.EmailField(max_length=50, null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=50)
    from_day = models.CharField(max_length=20)
    to_day = models.CharField(max_length=20)
    commitment_needed = models.IntegerField(default=2)

    def __str__(self):
        return self.title

