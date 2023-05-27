from django.urls import path
from .views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('init/', GoogleCalendarInitView.as_view(), name='google_calendar_init'),
    path('redirect/', GoogleCalendarRedirectView.as_view(), name='google_calendar_redirect'),
]
