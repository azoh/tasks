from django.contrib.auth.models import User
from django.db import models
import datetime
import random
from django.db.models.signals import post_save

def my_random_number():
    return random.randint(1,100)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(null=True, blank=True)
    random_number = models.IntegerField(null=True, blank=True, default=my_random_number)

    def age(self):
        if self.birthday > datetime.date.today().replace(year = self.birthday.year):
            return datetime.date.today().year - self.birthday.year - 1
        else:
            return datetime.date.today().year - self.birthday.year

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
