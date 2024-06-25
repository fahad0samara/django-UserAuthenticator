
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path("admin/", admin.site.urls),
    path("authUser/", include("django.contrib.auth.urls")),  # Built-in auth URLs
    path("authUser/", include("authUser.urls")),  # Custom app URLs
    
]
