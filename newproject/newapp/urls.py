from django.urls import path
from newapp import views
# from .views import home   // yesa bhi kr skte hai 


urlpatterns = [
    path('home/',views.home)
    # path('home/',home) 
    
]