from django.db import models

# Create your models here.
class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)