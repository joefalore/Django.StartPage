import datetime

from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=220, null=False, blank=False)
    phone = models.IntegerField(max_length=11)
    message = models.TextField(max_length=3000)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    
    def __unicode__(self):
        return self.email
    
    class Meta:
        ordering = ['-timestamp']
    