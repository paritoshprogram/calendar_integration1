from django.http import JsonResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from django.shortcuts import redirect
from django.views import View
from django.conf import settings

class GoogleCalendarInitView(View):
    def get(self, request):
        flow = Flow.from_client_config(
            settings.GOOGLE_OAUTH_CLIENT_CONFIG,
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri=request.build_absolute_uri('/rest/v1/calendar/redirect/')
        )
        authorization_url, _ = flow.authorization_url(access_type='offline')
        return redirect(authorization_url)

class GoogleCalendarRedirectView(View):
    def get(self, request):
        flow = Flow.from_client_config(
            settings.GOOGLE_OAUTH_CLIENT_CONFIG,
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri=request.build_absolute_uri('/rest/v1/calendar/redirect/')
        )
        flow.fetch_token(code=request.GET.get('code'))
        credentials = flow.credentials

        service = build('calendar', 'v3', credentials=credentials)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        # Process the events as per your requirement

        return JsonResponse({'events': events})

