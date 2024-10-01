"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from experience import urls as experience_urls
from users import urls as user_urls
from skill import urls as skill_urls
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(experience_urls)),
    path('api/', include(user_urls)),
    path('api/', include(skill_urls)),
    path('api/', include(blog_urls)),
]
