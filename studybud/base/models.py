from turtle import update
from venv import create
from django.db import models
from sqlalchemy import desc

class Room(models.Model):
    #host =
    #topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name