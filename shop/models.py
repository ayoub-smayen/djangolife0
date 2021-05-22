from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Simple single type product.
    """
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    prod_img=  models.ImageField(upload_to='products/') 
    quantity = models.IntegerField(default=20)
    remise_price   = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    description = models.TextField()
    rate = models.IntegerField()
    document = models.FileField(upload_to='generaldesc/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_price(self, request):
        return self.price

    
    @property
    def code(self):
        return str(self.id)