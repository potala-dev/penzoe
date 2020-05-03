from django.contrib import admin
from django.urls import path, include
from allauth.account.views import PasswordChangeView


class CustomPasswordChangeView(PasswordChangeView):
    success_url = '/'


urlpatterns = [
    path('tho/', admin.site.urls),
    path('', include('book.urls')),
    path('accounts/password/change/',
        CustomPasswordChangeView.as_view(),
        name="account_password_change"),
    path('accounts/', include('allauth.urls'))
]
