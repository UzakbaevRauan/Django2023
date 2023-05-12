from django.db import models
import sys
sys.path.append('/Users/User/Desktop/djangoproject/storeProject/Practice/users')
from  users.models import User


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 128, primary_key= True)
    address = models.CharField(max_length = 128)

class  MenuCategory(models.Model):
    name = models.CharField(max_length = 128, primary_key= True)
    restaurant = models.ForeignKey(to = Restaurant , on_delete=models.CASCADE)

class Dish(models.Model):
    name =models.CharField(max_length = 128)
    category =models.ForeignKey(to= MenuCategory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    
class Order(models.Model):
    dish = models.ForeignKey(to =Dish, on_delete=models.CASCADE)
    client_name =models.CharField(max_length = 128)
    date_ordered = models.DateField()
    restaurant = models.ForeignKey(to= Restaurant ,on_delete=models.CASCADE)

class Basket(models.Model):
    user = models.ForeignKey(to= User,on_delete=models.CASCADE)
    dish = models.ForeignKey(to=Dish, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Корзина товаров для {self.user.username}"
    def sum(self):
        return self.dish.price * self.quantity
