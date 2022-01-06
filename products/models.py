from io import BytesIO
from os import name
from PIL import Image

from django.core.files import File
from django.db import models

from sales.models import Sales



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering =('name',)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url

        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self,image,size=(150,150)):
        img = Image.open(image)
        (width,height) = (300,200)
        #resize all images to a standard size before generating thumbnails
        img.resize((width,height))
        img.convert('RGB')
        img.thumbnail(size)
        #saving image as file buffer in memory (mimicing a file)
        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        #reading converted thumbnail as a file and saving it in variable thumbnail
        thumbnail = File(thumb_io,name=image.name)

        return thumbnail

class Products(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    slug = models.SlugField()
    code = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    rate_in = models.DecimalField(max_digits=6,decimal_places=2)
    rate_out_retail = models.DecimalField(max_digits=6,decimal_places=2)
    rate_out_wholesale = models.DecimalField(max_digits=6,decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    pack_type = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'    


