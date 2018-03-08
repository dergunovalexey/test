from django.db import models


class ToDo(models.Model):
    qeust = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_quest = models.DateTimeField(blank=True)
    company = models.ForeignKey(to='core.Company', related_name='todos')
