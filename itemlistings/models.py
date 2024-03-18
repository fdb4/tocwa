from django.db import models

# Create your models here.
class main(models.Model):
    itemID=models.IntegerField(primary_key=True)
    itemName=models.CharField(max_length=75)
    Distributer=models.CharField(max_length=75)
    imagepath=models.CharField(max_length=200)
    categoryID=models.IntegerField()
    price=models.FloatField()
    manufacture=models.CharField(max_length=75)
    lastModifed=models.DateTimeField()
    class Meta:
        app_label='itemlistings'
    def __str__(self):
        return self.content