
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from listings.views import listing_list, listing_retrieve, listing_create, listing_update, listing_delete

urlpatterns = [
    path('admin/', admin.site.urls),
      path('', listing_list),
      path('add-listing/', listing_create),
      path('listings/<pk>/',  listing_retrieve),
      path('listings/<pk>/delete/',  listing_delete),
      path('listings/<pk>/edit/',  listing_update),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
