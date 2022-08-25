from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Gaurav Admin"
admin.site.site_title = "Sarmah Chat Site"
admin.site.index_title = "Welcome To Sarmah Chat Site"

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('admin/', admin.site.urls),
]
