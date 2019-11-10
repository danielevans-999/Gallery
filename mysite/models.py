from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    loc_name = models.CharField(max_length=30)
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_descprition = models.CharField(max_length=30)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def save_image(self):
        self.save
        
    def delete_image(self):
        self.delete()
        

    def __str__(self):
        return self.name