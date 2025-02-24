# # # *** Settings ***
# # # Library        SeleniumLibrary
# # # Library        RequestsLibrary
# # # Library        Collections

# # # *** Variables ***
# # # ${base_url}=    https://www.guvi.in    

# # # *** Test Cases ***
# # # Get Course ID
# # #     &{req_body}=        Create Dictionary    requestType=getCourseId    path=tamil/cloud-computing/aws-cloud-formation/    authtoken=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157
# # #     &{device_details}=  Create Dictionary    Device Model=Not detected    Device Type=desktop    OS=Windows 10    Browser=Chrome 132.0.0.0    Platform=Win32
# # #     Set To Dictionary    ${req_body}    deviceDetails=${device_details}    originUrl=www.guvi.in
# # #     ${response}=        POST        ${base_url}/courses/tamil/cloud-computing/aws-cloud-formation/   json=${req_body}    
# # #     Log    ${response.content}

# # *** Settings ***
# # Library           SeleniumLibrary
# # Library           RequestsLibrary
# # Library           Collections

# # *** Variables ***
# # ${base_url} =    https://www.guvi.in
# # ${api_endpoint} =  https://www.guvi.in/model/v2/course_details.php

# # *** Test Cases ***
# # Get Course ID
# #     &{req_body}=    Create Dictionary    requestType=getCourseId    path=tamil/cloud-computing/aws-cloud-formation/    authtoken=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157
# #     &{device_details}=    Create Dictionary    Device Model=Not detected    Device Type=desktop    OS=Windows 10    Browser=Chrome 132.0.0.0    Platform=Win32
# #     Set To Dictionary    ${req_body}    deviceDetails=${device_details}    originUrl=www.guvi.in

# #     ${response}=        POST    ${api_endpoint}    json=${req_body}
# #     Log    ${response.content}  # Log the entire response for debugging

# #     # Check the status code first for HTTP errors
# #     Should Be Equal As Integers    ${response.status_code}    200    # Check for 200 OK

# #     ${json_response}=    Convert To Dictionary    ${response.json()} # Convert to dictionary for easy access

# #     # Robustly check the 'status' and handle potential missing keys
# #     ${status}=    Get From Dictionary    ${json_response}    status    default=ERROR  # Default value if 'status' is missing
# #     Should Be Equal As Strings    ${status}    success    # Check for "success" or handle other expected values

# #     # Robustly get the course key
# #     ${course_details}=    Get From Dictionary    ${json_response}    courseDetails    default=[]  # Default empty list if missing
# #     ${course_key}=    Run Keyword And Ignore Error    Get From List    ${course_details}    0.key
# #     ${course_key}=    Set Variable If    '${course_key}'=='None'    'KEY_NOT_FOUND'    ${course_key}
# #     Log    Course Key: ${course_key}
# #     Should Be Equal As Strings    ${course_key}    awsCloudFormationTa    # Check for the expected key

# *** Settings ***
# Library           SeleniumLibrary
# Library           RequestsLibrary
# Library           Collections

# *** Variables ***
# ${base_url} =    https://www.guvi.in
# ${api_endpoint} =  https://www.guvi.in/model/v2/course_details.php

# *** Test Cases ***
# Get Course ID
#     &{req_body}=    Create Dictionary    requestType=getCourseId    path=tamil/cloud-computing/aws-cloud-formation/    authtoken=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157
#     &{device_details}=    Create Dictionary    Device Model=Not detected    Device Type=desktop    OS=Windows 10    Browser=Chrome 132.0.0.0    Platform=Win32
#     Set To Dictionary    ${req_body}    deviceDetails=${device_details}    originUrl=www.guvi.in

#     Log    Request Body: ${req_body}    level=DEBUG  # Log the request body

#     ${response}=        POST    ${api_endpoint}    json=${req_body}

#     Log    Status Code: ${response.status_code}    level=INFO # Log the status code immediately
#     Should Be Equal As Integers    ${response.status_code}    200    # Check for 200 OK

#     Log    Response Content: ${response.content}    level=DEBUG  # Log the FULL response content

#     ${json_response}=    Run Keyword And Ignore Error    Convert To Dictionary    ${response.json()}
#     # Check if conversion to dictionary was successful. If not, handle gracefully.
#     ${json_response}=    Set Variable If    '${json_response}'=='None'    '{"status":"error", "message":"Failed to parse JSON"}'    ${json_response}
#     ${json_response}=    Convert To Dictionary    ${json_response}

#     ${status}=    Get From Dictionary    ${json_response}    status    default=ERROR
#     Should Be Equal As Strings    ${status}    success    # Or handle other expected values

#     ${course_details}=    Get From Dictionary    ${json_response}    courseDetails    default=[]
#     ${course_key}=    Run Keyword And Ignore Error    Get From List    ${course_details}    0.key
#     ${course_key}=    Set Variable If    '${course_key}'=='None'    'KEY_NOT_FOUND'    ${course_key}
#     Log    Course Key: ${course_key}
#     Should Be Equal As Strings    ${course_key}    awsCloudFormationTa    # Check expected key

*** Settings ***
Library           SeleniumLibrary
Library           RequestsLibrary
Library           Collections

*** Variables ***
${base_url} =    https://www.guvi.in
${api_endpoint} =  https://www.guvi.in/model/v2/course_details.php

*** Test Cases ***
Get Course ID
    &{req_body}=    Create Dictionary    requestType=getCourseId    path=tamil/cloud-computing/aws-cloud-formation/    authtoken=4422222c9585fcbd6e93ffd97e555e197e17372b219542072547c57f83412de3aa93b8b6c0babb48b7cb6ceadbc2c2ad9c82510e5167c1b290d64706048ba157
    &{device_details}=    Create Dictionary    Device Model=Not detected    Device Type=desktop    OS=Windows 10    Browser=Chrome 132.0.0.0    Platform=Win32
    Set To Dictionary    ${req_body}    deviceDetails=${device_details}    originUrl=www.guvi.in

    Log    Request Body: ${req_body}    level=DEBUG  # Log the request body

    ${response}=        POST    ${api_endpoint}    json=${req_body}

    Log    Status Code: ${response.status_code}    level=INFO  # Correct log level
    Should Be Equal As Integers    ${response.status_code}    200    # Check for 200 OK

    Log    Response Content: ${response.content}    level=DEBUG  # Log the FULL response content

    ${json_response}=    Run Keyword And Ignore Error    Convert To Dictionary    ${response.json()}
    # Check if conversion to dictionary was successful. If not, handle gracefully.
    ${json_response}=    Set Variable If    '${json_response}'=='None'    '{"status":"error", "message":"Failed to parse JSON"}'    ${json_response}
    ${json_response}=    Convert To Dictionary    ${json_response}

    ${status}=    Get From Dictionary    ${json_response}    status    default=ERROR
    Should Be Equal As Strings    ${status}    success    # Or handle other expected values

    ${course_details}=    Get From Dictionary    ${json_response}    courseDetails    default=[]
    ${course_key}=    Run Keyword And Ignore Error    Get From List    ${course_details}    0.key
    ${course_key}=    Set Variable If    '${course_key}'=='None'    'KEY_NOT_FOUND'    ${course_key}
    Log    Course Key: ${course_key}
    Should Be Equal As Strings    ${course_key}    awsCloudFormationTa    # Check expected key