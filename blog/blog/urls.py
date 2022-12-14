"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from  core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.home, name="home"),
    path('about/',core_views.about, name="about"),
    path('blog/',core_views.blog, name="blog"),
    path('blogdetalle/',core_views.blogdetalle, name="blogdetalle"),
    path('login/',include('core.urls')),
    path('registrarse/',core_views.registrarse, name="registrarse"),
    # path('login/',core_views.login, name="login"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)