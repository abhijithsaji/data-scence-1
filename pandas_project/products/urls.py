from django.urls import path
from .views import *
app_name = 'products'

urlpatterns = [
    path('',chart_select_view, name = 'main-products-view')
]



