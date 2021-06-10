from django.db import models

class Data_of_rows(models.Model):
    standard_img = models.ImageField(upload_to = 'images/' , default = "")
    standard =  models.CharField(max_length = 20)
    description = models.CharField(max_length =115)

    def __str__(self):
        return self.standard

# Create your models here.





