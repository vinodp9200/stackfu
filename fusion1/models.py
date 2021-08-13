from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class userform(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField()
    email=models.EmailField(max_length=50)
    phone_number= models.CharField(max_length=12)  # validators should be a list

    def isExists(self):
        if userform.objects.filter(email = self.email):
            return True

        return  False
