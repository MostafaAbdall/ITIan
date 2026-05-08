from django.db import models

# Create your models here.
class Course(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)
    Code = models.CharField(max_length=10, null=False)
    Track = models.CharField(max_length=100, null=False)
    Created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    Updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.Name