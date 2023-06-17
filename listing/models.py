from django.db import models

class Listings(models.Model):
    Title = models.CharField(max_length=100,null=False)
    Address = models.TextField(max_length=250,null=False)
    Area = models.IntegerField(null=True)
    Description = models.TextField()
    media = models.ImageField(upload_to="media",null=False)

    def __str__(self):
         return self.Title


class Contact(models.Model):
    name = models.CharField(max_length=40,null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10,null=False)
    enquiry = models.ForeignKey(Listings, on_delete=models.CASCADE,null=True)
    message = models.TextField(max_length=250)
    Address = models.TextField(max_length=250)

 
    def __str__(self):
            return self.name

            
        