from django.contrib import admin
from django.urls import path
from App1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('add/<int:id>',views.addqn,name='addq'),
    path('delete/<int:id>',views.delete_record,name='pdel'),
    path('create/product',views.create_product,name="cp"),
    path('sale/<int:id>',views.product_sale,name="psale"),
    path('salelist',views.sale_list,name="lsale"),
    path('edit/product/<int:id>',views.edit_product,name="ep")
]
