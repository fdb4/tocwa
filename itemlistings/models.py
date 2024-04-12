from django.db import models

# Create your models here.
class Main(models.Model):
    itemID=models.PositiveIntegerField(primary_key=True)
    itemName=models.CharField(max_length=75)
    Distributer=models.CharField(max_length=75)
    imagepath=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    manufacture=models.CharField(max_length=75)
    lastModifed=models.DateTimeField(auto_now_add=True)
    categoryID=models.ForeignKey('Category',related_name="items",on_delete=models.RESTRICT,db_column='categoryID')

  #  class Meta:
   #     app_label='itemlistings'
    def __str__(self):
        return self.content
class Category(models.Model):
    categoryID=models.PositiveIntegerField(primary_key=True)
    categoryName=models.CharField(max_length=70)
    def __str__(self):
        return self.content

class Cartitem(models.Model):
    cartItemID=models.PositiveIntegerField(primary_key=True)
    cartID=models.ForeignKey('Cart',related_name='+',on_delete=models.RESTRICT,db_column='cartID')
    itemID=models.ForeignKey('Main',related_name='+',on_delete=models.RESTRICT,db_column='itemID')
    quantity=models.PositiveIntegerField()
    def __str__(self):
        return self.content
class Cart(models.Model):
    cartID=models.PositiveIntegerField(primary_key=True)
    userName=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pickupdelv=models.BooleanField()
    address=models.CharField(max_length=100)
    LastModified=models.DateTimeField(auto_now_add=True)
    list_display=('cartID')
    def __str__(self):
        return self.content