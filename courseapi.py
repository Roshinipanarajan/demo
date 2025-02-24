# import requests

# url = "https://www.guvi.in/model/v2/course_details.php"

# payload = 'myData=%7B%22requestType%22%3A%22getCourseId%22%2C%22path%22%3A%22malayalam%2Fprogramming%2Fpython-zero-to-hero%2F%22%2C%22authtoken%22%3A%22f988540b2625b5946e0d2b1c93456349581002656ed02e741183d80171348bf22a17cbcf966582ab949c8749b2a962f10e09ca3886f8bc0fe32ed4749f2ed490%22%2C%22deviceDetails%22%3A%22Device%20Model%3A%20Not%20detected~~Device%20Type%3A%20desktop~~OS%3A%20Windows%2010~~Browser%3A%20Chrome%20133.0.0.0~~Platform%3A%20Win32%22%2C%22originUrl%22%3A%22www.guvi.in%22%7D'
# headers = {
#   'Accept': 'text/plain',
#   'Content-Type': 'application/x-www-form-urlencoded'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

import requests
import urllib.parse

authtoken= "ede8ec0c23bd49ab1e3a3d9f0d6315891699825ede6dd001dba5b6fafe6bc5694eb4bb2f220bcfef68430f5607c9931a8b530fcc7e1b9a89b3bcb10573e2abae"


# Function to send request with URL-encoded payload
def get_course_details(path, authtoken):
    url = "https://www.guvi.in/model/v2/course_details.php"

    # Define the payload dictionary (human-readable format)
    payload_dict = {
        "requestType": "getCourseId",
        "path": path,
        "authtoken": authtoken,
        "deviceDetails": "Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 133.0.0.0~~Platform: Win32",
        "originUrl": "www.guvi.in"
    }

    # Encode the payload to URL format
    encoded_payload = "myData=" + urllib.parse.quote_plus(str(payload_dict).replace("'", '"'))

    headers = {
        'Accept': 'text/plain',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=encoded_payload)

    return response.text  # Return API response

# Example usage
path = "malayalam/programming/python-zero-to-hero/"
response_text = get_course_details(path, authtoken)
print(response_text)
