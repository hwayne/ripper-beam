from django.db import models

class Route(models.Model):
    key = models.CharField(max_length=16, unique=True)
    url = models.CharField(max_length=128)
    auth_username = models.CharField(max_length=128)
    auth_password = models.CharField(max_length=128)

    def __str__(self):
        return "{}: {}".format(self.key, self.url)
