# *** Settings ***
# Library    Collections
# Library    RequestLibrary

# *** Variables ***
# ${API_URL}    https://www.guvi.in/model/v2/course_details.php

# &{HEADERS}  
# ...    Content-Type=application/json  
# ...    Authorization=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157  # Token from JSON  

# &{PAYLOAD}  
# ...    requestType=getCourseId  
# ...    path=tamil/cloud-computing/aws-cloud-formation/  
# ...    authtoken=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157  
# ...    deviceDetails=Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 132.0.0.0~~Platform: Win32  
# ...    originUrl=www.guvi.in  

# *** Test Cases ***
# Add Guvi URL into Library Database
# ${response} =    POST    ${API_URL}    json=${PAYLOAD}    headers=${HEADERS}  
#     Log    ${response.json()}  
#     Should Be Equal As Strings    ${response.status_code}    200

*** Settings ***
Library    Collections
Library    RequestsLibrary

*** Variables ***
${API_URL}    https://www.guvi.in/model/v2/course_details.php  

&{HEADERS}  
...    Content-Type=application/json  
...    Authorization=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157  

&{PAYLOAD}  
...    requestType=getCourseId  
...    path=tamil/cloud-computing/aws-cloud-formation/  
...    authtoken=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157  
...    deviceDetails=Device Model: Not detected~~Device Type: desktop~~OS: Windows 10~~Browser: Chrome 132.0.0.0~~Platform: Win32  
...    originUrl=www.guvi.in  

*** Test Cases ***
Add Guvi URL into Library Database
    ${response} =    POST    ${API_URL}    json=${PAYLOAD}    headers=${HEADERS}  
    Log    ${response.json()}  
    Should Be Equal As Strings    ${response.status_code}    200
