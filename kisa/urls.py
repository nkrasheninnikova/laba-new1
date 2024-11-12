from django.urls import path
from .views import index
app_name = 'kisa'
urlpatterns = [
path('', index, name='index')
]