*** Settings ***
Documentation    To Validate the login Page
Library          SeleniumLibrary
Test Teardown    Close Browser

*** Variables ***
${Error-message}    css:.invalid-feedback

*** Test Cases ***
Validate successful Login
    Open the browser with the Guvi url
    Fill the login form
    Wait until it checks and display error message
    Verify the error message is correct

*** Keywords ***
 Open the browser with the Guvi url
     Create Webdriver    Chrome
     Go To               https://www.guvi.in/sign-in/
     Maximize Browser Window
Fill the login form
    Input Text        id:email       gandhamathan@guvi.in
    Input Password    id:password    12345678
    Click Element     id:login-btn 

Wait until it checks and display error message
    Wait Until Element Is Visible    ${Error-message}

Verify the error message is correct
    # ${result}=    Get Text    ${Error-message}
    # Should Be Equal As Strings    ${result}    Incorrect Email or Password 
    Element Text Should Be    ${Error-message}    Incorrect Email or Password

