import profile
from django.db import models

# Create your models here.
class Author(models.Model):
        name=models.CharField(max_length=250)
        def __str__(self):
          return self.name


class Book(models.Model):
    name=models.CharField(max_length=250)
    puplishDate=models.DateField()
    AddToSiteAt=models.DateTimeField(auto_now_add=True)
    img=models.CharField(max_length=250)
    price=models.DecimalField(
                         max_digits = 5,
                         decimal_places = 2)
    appropriate=models.CharField(max_length=250 ,choices=[("<8","under 8"),("8:15","from 8 to 15"),(">15","adult")],default=">15")
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
       return self.name


