from django.urls import path, re_path
from intro.views import *

urlpatterns = [
    path('', homepage),
    path('intro/', homepage),
    path('intro/contact/', contact),
    path('intro/biosketch/', biosketch),
    path('intro/portfolio/', portfolio),
    path('intro/links/', links),
]