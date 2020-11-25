from django.db import models

# Create your models here.
class Bookmark(models.Model) :
    title= models.CharField(("Title"), max_length=100,blank=True)
    url = models.URLField(("URL"), max_length=200)

    def __str__(self):
        return self.title
        
    