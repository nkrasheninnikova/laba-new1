from django.urls import path
from .views import index
from .views import other_page
from .views import BBLoginView
from .views import profile

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', other_page, name='other'),
path('account/login', BBLoginView.as_view(),name='login'),
path('account/profile/', profile, name='profile'),

]
