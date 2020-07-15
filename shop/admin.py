from django.contrib import admin
from .models import Product,Order

# Register your models here.

admin.site.site_header = "vinay E-Commerce-Site"
admin.site.site_title = "Gadgets Shop"
admin.site.index_title = "Manage Gadgets Shoping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,requesst,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = "default category"    
    list_display = ('title','price','discount_price','category','discription')
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)
    fields = ('title','price',)
    list_editable = ('price','category',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
