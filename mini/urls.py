from django.urls import path
from mini.views import home, about, category, portfolio, blog, contact, login, register

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('category/', category, name='category'),
    path('portfolio/', portfolio, name='portfolio'),
    path('blog/', blog, name='blog'),

    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),

    path('register/', register, name='register'),


]

