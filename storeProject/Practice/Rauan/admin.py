from django.contrib import admin

from.models import Restaurant,MenuCategory, Dish, Order,Basket

admin.site.register(Basket)
admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(Dish)
admin.site.register(Order)

class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','quantity', 'price']
    fields = ('name', ('price', 'quantity'),'category',)
    search_fields = ('name',)
    ordering = ('name',)
