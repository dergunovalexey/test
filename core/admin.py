from django.contrib import admin
from core import models

for model in models.__all__:
    admin.site.register(getattr(models, model))

