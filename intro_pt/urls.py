from django.urls import path, re_path
from intro_pt.views import *


urlpatterns = [
    path('intro_pt/', homepage_pt),
    path('intro_pt/contact/', contact_pt),
    path('intro_pt/biosketch/', biosketch_pt),
    path('intro_pt/portfolio/', portfolio_pt),
    path('intro_pt/links/', links_pt),
]