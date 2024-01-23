import requests
import os
import atexit
import msal
import logging

clientId = 'xxx'
username = 'xxx@xxx.onmicrosoft.com'

logging.getLogger("msal").setLevel(logging.WARN)

scope = ["User.Read", "User.ReadBasic.All"]

accessToken = None

cache = msal.SerializableTokenCache()
if os.path.exists("token_cache.bin"):
    cache.deserialize(open("token_cache.bin", "r").read())
atexit.register(lambda:
                open("token_cache.bin", "w").write(cache.serialize())
                if cache.has_state_changed else None)

app = msal.PublicClientApplication(
    clientId,
    client_credential=None,
    token_cache=cache,
    authority="https://login.microsoftonline.com/common")

def get_login():
    global accessToken
    result = None
    accounts = app.get_accounts(username=username)
    if accounts:
        print("Pick the account you want to use to proceed:")
        for a in accounts:
            print(a["username"])
        chosen = accounts[0]
        result = app.acquire_token_silent(scope, account=chosen)
    
    if not result:
        result = app.acquire_token_interactive(scopes=scope, login_hint=username)
        if "access_token" in result:
            accessToken = result['access_token']
        else:
            print(result.get("error"))
            print(result.get("error_description"))
            print(result.get("correlation_id"))
    else:
        accessToken = result['access_token']
    
def get_me():
    url = 'https://graph.microsoft.com/v1.0/me'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(response.json())
    
get_login()

get_me()
