from django.db import models

# Create your models here.

TYPES_PURPOSE = (
    ('Sale','SALE'),
    ('Rent','RENT'),
)

TYPES_PROPRTY = (
    ('House','HOUSE'),
    ('Flat','FLAT'),
    ('Shop','SHOP'),
)


class Property(models.Model):
    owner = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    address = models.TextField()
    image1 = models.ImageField(upload_to='propert/',blank=True)
    image2 = models.ImageField(upload_to='propert/',blank=True)
    image3 = models.ImageField(upload_to='propert/',blank=True)
    image4 = models.ImageField(upload_to='propert/',blank=True)
    type = models.CharField(max_length=5,choices=TYPES_PROPRTY,default=None)
    purpose = models.CharField(max_length=4,choices=TYPES_PURPOSE,default=None)
    price = models.CharField(max_length=10)
    describ = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner
    
    