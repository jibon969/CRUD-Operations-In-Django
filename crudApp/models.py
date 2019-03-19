from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dept = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated']

