from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product/<str:slug>/', product_detail,name="product_detail_url"),
    path('thanks/', thanks, name='thanks_url' ),
    path('gallery/', gallery , name='gallery_url'),
    path('about/', about, name='about_url'),
    path('message/', send_message, name="send_message_url"),
    path('', products_list, name='products_list_url'),
]