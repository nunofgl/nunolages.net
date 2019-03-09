"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import intro.urls
import intro_pt.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/', include('intro.urls')),
    path('', include('intro_pt.urls')),
    # For zinnia
    path('weblog/', include('zinnia.urls')),
    path('comments/', include('django_comments.urls')),
    ## optional zinnia urls
    path('', include('zinnia.urls.capabilities')),
    path('', include('intro.urls')),
    path('search/', include('zinnia.urls.search')),
    path('sitemap/', include('zinnia.urls.sitemap')),
    path('trackback/', include('zinnia.urls.trackback')),
    path('@myblog/tags/', include('zinnia.urls.tags')),
    path('blog/feeds/', include('zinnia.urls.feeds')),
    path('blog/random/', include('zinnia.urls.random')),
    path('blog/author/', include('zinnia.urls.authors')),
    path('blog/categories/', include('zinnia.urls.categories')),
    path('blog/comments/', include('zinnia.urls.comments')),
    path('blog/', include('zinnia.urls.entries')),
    path('blog/', include('zinnia.urls.archives')),
    path('blog/', include('zinnia.urls.shortlink')),
    path('blog/', include('zinnia.urls.quick_entry')),
]
