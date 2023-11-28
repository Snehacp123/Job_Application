from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Job application URLs
    path('jobapp/', include("jobapp.urls"))

]
