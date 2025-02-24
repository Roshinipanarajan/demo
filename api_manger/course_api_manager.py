import json
import urllib.parse

courseurl = "https://www.guvi.in/model/v2/course_details.php"

#it accepting my encoded payload
def get_encoded_payload(path, authtoken):
    """Dynamically generates URL-encoded payload"""
    coursepayload = {
        "requestType": "getCourseId",
        "path": path,
        "authtoken": authtoken,
        "deviceDetails": "Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 133.0.0.0~~Platform: Win32",
        "originUrl": "www.guvi.in"
    }
    return "myData=" + urllib.parse.quote_plus(json.dumps(coursepayload))

courseheaders = {
    'Accept': 'text/plain',
    'Content-Type': 'application/x-www-form-urlencoded'
}


