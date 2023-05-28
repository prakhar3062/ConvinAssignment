import os
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

# This variable specifies the name of a file that contains the OAuth 2.0
# information for this application, including its client_id and client_secret.
CLIENT_SECRETS_FILE = os.environ.get("CLIENT_SECRETS_FILE", "credentials.json")

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection and REDIRECT URL.
SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/userinfo.profile',
          'openid']
REDIRECT_URL = os.environ.get("REDIRECT_URL", 'http://127.0.0.1:8080/rest/v1/calendar/redirect')
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

def initialize_flow(session, scopes, redirect_url, client_secret_file):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        client_secret_file, scopes=scopes)
    flow.redirect_uri = redirect_url
    # Store the state so the callback can verify the auth server response.
    session['state'] = flow.state
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')
    return authorization_url, state

@api_view(['GET'])
def GoogleCalendarInitView(request):
   
