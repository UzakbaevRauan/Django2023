from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 128, primary_key= True)
    address = models.CharField(max_length = 128)

class  MenuCategory(models.Model):
    name = models.CharField(max_length = 128, primary_key= True)
    restaurant = models.ForeignKey(to = Restaurant , on_delete=models.CASCADE)

class Dish(models.Model):
    name =models.CharField(max_length = 128, unique= True)
    
    category =models.ForeignKey(to= MenuCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
class Order(models.Model):
    dish = models.ForeignKey(to =Dish, on_delete=models.CASCADE)
    client_name =models.CharField(max_length = 128)
    date_ordered = models.DateField()
    restaurant = models.ForeignKey(to= Restaurant ,on_delete=models.CASCADE)