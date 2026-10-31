from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    # Maps http://127.0.0.1:8000/api/hello/ to your hello view
    path('hello/', views.hello, name='hello'),
]