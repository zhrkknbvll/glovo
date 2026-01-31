from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем твоё приложение (ИСПРАВЛЕНО на glovo_app)
    path('', include('glovo_app.urls')),

    # Для авторизации (allauth)
    path('accounts/', include('allauth.urls')),
]

# Добавляем пути для медиа-файлов (картинки магазинов и товаров)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)