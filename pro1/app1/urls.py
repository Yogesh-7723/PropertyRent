from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('base/',views.base),
    path('about/',views.about),
    path('contact/',views.contact),
    path('user_login/',views.user_login),
    path('user_logout/',views.user_logout),
    path('user_register/',views.register),
    path('view_pro/',views.view_pro),
    path('house/',views.house),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

