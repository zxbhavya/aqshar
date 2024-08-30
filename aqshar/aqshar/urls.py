from django.contrib import admin
from django.urls import path
from . import settings
from core import views
from django.urls import path, include
from core.views import chat, index, login_user, catalogue, signup, checkout, donate, account, orders, donating, selling
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("core/", include("core.urls")),
    path("chat/", chat, name="chat"),
    path("login/", login_user, name="login"),
    path("catalog/", catalogue, name="catalog"),
    path("signup/", signup, name="signup"),
    path("checkout/",checkout, name="checkout"),
    path("donate/", donating, name="donating"),
    path('sell/', selling, name='selling'),
    path('account/', account, name='account'),
    path('orders', orders, name='orders'),
    path("admin/", admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

