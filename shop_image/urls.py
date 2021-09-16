from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("paystack", include(('paystack.urls', 'paystack'), namespace='paystack')),
    path("users/", include("users.urls")),
    path("images/", include("images.urls")),
    path("payments/", include("payments.urls")),
    path("", index, name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
