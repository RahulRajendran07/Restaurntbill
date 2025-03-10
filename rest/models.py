from django.db import models

# Create your models here.

class Category(models.Model):

    name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):

    title=models.CharField(max_length=120,unique=True)

    description=models.TextField()

    price=models.DecimalField(max_digits=5,decimal_places=2)

    category_object=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="items")

    def __str__(self):
        return self.title
    
class Table(models.Model):
    table_name = models.CharField(max_length=50, unique=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.table_name

class Order(models.Model):

    created_at=models.DateTimeField(auto_now_add=True)

    status=models.BooleanField(default=False)

    total=models.DecimalField(max_digits=8,decimal_places=2,null=True)

    table = models.ForeignKey(Table,on_delete=models.CASCADE)

class OrderItems(models.Model):


    order_object=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")

    item_object=models.ForeignKey(Item,on_delete=models.CASCADE)

    qty=models.DecimalField(max_digits=6,decimal_places=3)

    price = models.DecimalField(max_digits=7,decimal_places=3)
