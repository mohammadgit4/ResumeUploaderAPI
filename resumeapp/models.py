from django.db import models

STATE_CHOICE = (
    ('1', 'Gujrat'),
    ('2', 'Rajasthan'),
    ('3', 'Maharastra')
)

class Profile(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    dob = models.DateField(verbose_name='Date Of Birth')
    state = models.CharField(choices=STATE_CHOICE, max_length=15)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    pimage = models.ImageField(verbose_name='Profile Image', upload_to='pimage')
    rdoc = models.FileField(verbose_name='Resume Doc', upload_to='rdocs')