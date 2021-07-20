from __future__ import unicode_literals
from django.contrib import admin
from .models import UserPublicDetails, UserPrivateData

admin.site.register(UserPublicDetails)
admin.site.register(UserPrivateData)
