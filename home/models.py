from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save                                      


# Create your models here.
class UserDetail(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.EmailField(unique=True)
    user_mobile = models.CharField(max_length=15)
    user_dob = models.DateField()
    user_gender = models.CharField(max_length=10)
    user_myfile = models.ImageField(upload_to='file_images/')

    def __str__(self):
        return self.user_name

class Registration(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    gender = models.CharField(max_length=10)
    dob = models.DateField(null=True)
    password = models.CharField(max_length=15)

    def fun(self, *args, **kwargs):
        post_save.send(Registration, instance=self, created=True, pwd=args[0])
        super(Registration,self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name

class StudentDetail(models.Model):
    student_name = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=10)
    father_name = models.CharField(max_length=30)
    pass_fail = models.CharField(max_length=5)

    def __str__(self):
        return self.roll_no
    