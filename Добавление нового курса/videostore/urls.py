from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name='reg'),
    path('', include('courses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
