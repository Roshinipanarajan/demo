import json

loginurl = "https://www.guvi.in/model/v2/login_details.php"

def get_login_payload(authtoken):
    """Returns a properly formatted JSON payload for login request"""
    loginpayload = {
        "auth": authtoken,
        "deviceDetails": "Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 133.0.0.0~~Platform: Win32",
        "originUrl": "www.guvi.in"
    }
    return json.dumps(loginpayload)

loginheaders = {
  'Accept': 'text/plain',
  'Content-Type': 'text/html'
}
