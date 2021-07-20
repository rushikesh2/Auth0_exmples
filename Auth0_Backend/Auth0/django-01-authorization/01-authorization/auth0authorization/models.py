from __future__ import unicode_literals
from django.db import models
import jsonfield


class UserPublicDetails(models.Model):
    shirts = models.CharField(max_length=200, null=False, blank=True)
    trousers = models.CharField(max_length=200, null=False, blank=True)
    shoes = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self):
        return str(self.trousers) + ',' + str(self.shoes) + ',' + str(self.shirts)


class UserPrivateData(models.Model):
    name = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=50, null=False, blank=True)
    email = models.CharField(max_length=50, null=False, blank=True)
    # personal_shirts = models.CharField(max_length=300, null=True)
    # personal_trousers = models.CharField(max_length=300, null=True)
    # personal_shoes = models.CharField(max_length=300, null=True)
    # cloth_type = models.CharField(max_length=200, null=True)
    data = jsonfield.JSONField(null=True)

    def __str__(self):
        return str(self.name) + ', ' + str(self.nickname) + ', ' + ', ' + str(self.email) + ', ' + str(self.data)

        # return str(self.name) + ', ' + str(self.personal_shirts) + ', ' + str(self.personal_trousers) + ', ' + str(
        #     self.personal_shoes) + ', ' + str(self.nickname) + ', ' + str(self.personal_shoes) + ', ' + str(
        #     # self.email) + ', ' + str(self.cloth_type)
