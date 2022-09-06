from django.urls import path

from .views import LoginFormView, LogoutView

app_name = 'core'

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
    # path('logout/', LogoutRedirectView.as_view(), name='logout')
]