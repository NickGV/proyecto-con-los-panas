# mi_aplicacion/models.py

from django.db import models

class tasks(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    creation_date= models.DateTimeField(auto_now_add=True)    
    status = models.CharField(max_length=20, default='Pending')
    def __str__(self):
        return self.title
                