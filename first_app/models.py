from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(, max_length=100)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name

    

    



# Create your models here.
