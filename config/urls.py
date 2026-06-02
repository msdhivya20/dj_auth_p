from django.contrib import admin
from django.urls import path, include
from .views import landing, home

urlpatterns = [

   
    path('admin/', admin.site.urls),

    # Landing Page
    path('', landing, name='landing'),

    # Dashboard Home
    path('home/', home, name='home'),

 
    # Accounts
    path('', include('accounts.urls')),

    path('', include('ml.urls')),

]
