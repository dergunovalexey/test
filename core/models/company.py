from django.conf import settings
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='companies',
        through='core.CompanyUserMap'
    )
    def __repr__(self):
        return 'Company: {name}'.format(name=self.name)

    def __str__(self):
        return '{name}'.format(name=self.name)


class CompanyUserMap(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    company = models.ForeignKey(to='core.Company')
