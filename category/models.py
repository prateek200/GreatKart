from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.

class category(models.Model):
    category_name = CharField(max_length = 50, unique = True)
    slug = CharField(max_length =  100 , unique = True)
    description = TextField(max_length =  255, blank =  True)
    cat_image = ImageField(upload_to = 'photos/category', blank = True) 

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name