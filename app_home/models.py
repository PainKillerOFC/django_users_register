from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)