from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering =('name',)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/{self.slug}/'


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