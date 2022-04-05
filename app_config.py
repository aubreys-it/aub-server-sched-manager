import os

CLIENT_ID = "f296c189-c551-4674-8388-164d9ee53b6f" # Application (client) ID of app registration

AUTHORITY = "https://login.microsoftonline.com/64edf217-1246-405a-a5bc-c1922d9184e2"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/64edf217-1246-405a-a5bc-c1922d9184e2"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/me'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.Read.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
