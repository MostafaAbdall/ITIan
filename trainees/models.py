from django.db import models

# Create your models here.

class Trainee(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)
    Age = models.IntegerField(null=False)
    Email = models.EmailField(null=False)
    Phone = models.CharField(max_length=11, null=False)
    Degree = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.Name