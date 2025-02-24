# import json
# import requests

# header = {
#     'Content-Type' : 'text/html'
# }

# request_payload = {
#     "requestType": "getCourseId",
#     "path": "tamil/cloud-computing/aws-cloud-formation/",
#     "authtoken": "4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157",
#     "deviceDetails": "Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 133.0.0.0~~Platform: Win32",
#     "originUrl": "www.guvi.in"
# }
import json
import requests

header = {
    'Accept': 'text/plain',
  'Content-Type': 'text/html'
}

request_payload = {
    # "requestType": "getCourseId",
    # "path": "tamil/cloud-computing/aws-cloud-formation/",
    "auth": "f988540b2625b5946e0d2b1c93456349581002656ed02e741183d80171348bf22a17cbcf966582ab949c8749b2a962f10e09ca3886f8bc0fe32ed4749f2ed490",
    "deviceDetails": "Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 133.0.0.0~~Platform: Win32",
    "authtoken":"f988540b2625b5946e0d2b1c93456349581002656ed02e741183d80171348bf22a17cbcf966582ab949c8749b2a962f10e09ca3886f8bc0fe32ed4749f2ed490",
    "originUrl": "www.guvi.in"
}

def post_request(url, headers=None, payload=None):    
    """    Perform a POST request to the specified URL with optional headers and payload.    
    If the response status is not in the 200-299 range, raises an HTTPError.    
    Logs any errors and raises exceptions to fail the scenario.    """    
    try:        
        response = requests.request("POST", url, headers=headers, data=payload)        
        # response.raise_for_status()        
        return response    
    except requests.exceptions.HTTPError as http_err:        
        print("http error occure")
        raise

# def pretty(response):
#     return json.dumps(response.json(),indent=1,sort_keys=True)

# try: 
#     print(header)
#     response= post_request("https://www.guvi.in/model/v2/course_details.php",headers=header,payload= request_payload)
#     pretty_response= pretty(response)
#     print(pretty_response)
# except:
#     print("http response")
    # response= requests.request("POST", )

# # response = requests.post("https://www.guvi.in/model/v2/course_details.php", 
# #                         headers= header,
# #                         json=request_payload)

# # # print(response.status_code)
# # print(response.text)
# # print(response.status_code)

# # if response.status_code == 200:
# #     try:
# #         # data = response.json()
# #         print(data)
# #     except requests.exceptions.JSONDecodeError:
# #         print("Error: Server returned non-JSON content.  Check response.text")
# #         print(response.text)  
# # elif response.status_code == 401:
# #     print("Error: Unauthorized. Check your authtoken.")
# #     print(response.text)
# # elif response.status_code == 404:
# #     print("Error: Not Found. Check URL or path.")
# #     print(response.text)
# # elif response.status_code == 500:
# #     print("Error: Internal Server Error. Check server logs.")
# #     print(response.text)
# # else:
# #     print(f"Error: Unexpected status code {response.status_code}")
# #     print(response.text)

import json
import requests

header = {
    'Accept': 'text/plain',
  'Content-Type': 'text/html'
}

request_payload = {
    # "requestType": "getCourseId",
    # "path": "tamil/cloud-computing/aws-cloud-formation/",
    "auth": "f988540b2625b5946e0d2b1c93456349581002656ed02e741183d80171348bf22a17cbcf966582ab949c8749b2a962f10e09ca3886f8bc0fe32ed4749f2ed490",
    "deviceDetails": "Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 133.0.0.0~~Platform: Win32",
    "authtoken":"f988540b2625b5946e0d2b1c93456349581002656ed02e741183d80171348bf22a17cbcf966582ab949c8749b2a962f10e09ca3886f8bc0fe32ed4749f2ed490",
    "originUrl": "www.guvi.in"
}

# def post_request(url, headers=None, payload=None):    
#     """Perform a POST request to the specified URL with optional headers and payload."""    
#     try:        
#         response = requests.post(url, headers=headers, json=payload)  # Use `json=payload` instead of `data=payload`
#         response.raise_for_status()  # Raises an error for non-200 responses        
#         return response    
#     except requests.exceptions.HTTPError as http_err:        
#         print(f"HTTP error occurred: {http_err}")  # More informative message
#         raise
#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error occurred: {req_err}")
#         raise

# def post_request(url, headers=None, payload=None):    
#     """Perform a POST request to the specified URL with optional headers and payload."""    
#     try:        
#         response = requests.post(url, headers=headers, json=payload)
#         response.raise_for_status()  # Raises an error for HTTP codes 400+
        
#         print("Raw response content:", response.text)  # Print response before parsing JSON
        
#         return response    
#     except requests.exceptions.HTTPError as http_err:        
#         print(f"HTTP error occurred: {http_err}")  
#         raise
#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error occurred: {req_err}")
#         raise

# def pretty(response):
#     """Formats JSON response into a pretty-printed string."""
#     return json.dumps(response.json(), indent=2, sort_keys=True)

# try: 
#     print("Sending request with headers:", header)
#     response = post_request("https://www.guvi.in/model/v2/course_details.php", header, request_payload)
#     pretty_response = pretty(response)
#     print(pretty_response)
# except Exception as e:
#     print(f"An error occurred: {e}")
