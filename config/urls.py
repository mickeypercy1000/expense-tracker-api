from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('swagger.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
    path('user/', include("user.urls"))
]
