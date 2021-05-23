from allauth.account.views import PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


class CustomPasswordChangeView(PasswordChangeView):
    success_url = "/"


urlpatterns = [
    path(settings.ADMIN_PATH + "/", admin.site.urls),
    path("", include("penzoe.core.urls")),
    path("users/", include("penzoe.users.urls")),
    path("discourse/", include("penzoe.discourse.urls")),
    path(
        "accounts/password/change/",
        CustomPasswordChangeView.as_view(),
        name="account_password_change",
    ),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    if settings.DEBUG_TOOLBAR:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
