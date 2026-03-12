from django.urls import path
from .views import home, first, product, contact, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', first, name='first'),
    path('home', home, name='home'),
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 86c38f3 (Updating files to friend's repository)
    path('product', product, name='products'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
<<<<<<< HEAD
=======
  path('product', product, name='products'),
  path('about', about, name='about'),
  path('contact', contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 0a42598d478252253a86aabd558b58b3ed4bed23
=======
>>>>>>> 86c38f3 (Updating files to friend's repository)
