from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poem(models.Model):
    created = models.DateTimeField()

class Line(models.Model):
    poem = models.ForeignKey(Poem)
    text = models.CharField(max_length=256, blank=True, null=False)
