
from src.kokkaiapiclient.api_client import ApiClient
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider)

def get_client() -> ApiClient:
    auth_provider = AnonymousAuthenticationProvider()
    request_adapter = HttpxRequestAdapter(auth_provider)
    client = ApiClient(request_adapter=request_adapter)
    return client