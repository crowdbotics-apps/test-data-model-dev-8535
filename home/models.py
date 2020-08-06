from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title_update = models.CharField(max_length=150, blank=True,)
    first_update = models.CharField(max_length=256, null=True, blank=True,)
    last_update = models.CharField(max_length=256, null=True, blank=True,)
    new_address = models.TextField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    bodyTest = models.TextField(blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
