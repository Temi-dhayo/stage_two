from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Person(models.Model):
    name = models.CharField(_("name"), max_length=50,unique=True)

    def __str__(self):
        return self.name