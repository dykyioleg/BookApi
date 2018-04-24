from django.db import models
from django.conf import settings
# Create your models here.


class Book(models.Model):
    author         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title          = models.CharField(max_length=120, null=True, blank=True)
    description    = models.TextField(max_length=120, null=True, blank=True)
    timestamp      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author.username)


    @property
    def owner(self):
        return self.author

