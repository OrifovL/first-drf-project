from django.db import models

# Create your model

class Products(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(auto_now_add=True)
    