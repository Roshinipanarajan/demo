*** Settings ***
Documentation    To Validate the login Page
Library          SeleniumLibrary
Resource         resource.robot
Test Setup       Open the browser with the Guvi url
Test Teardown    Close Browser
*** Test Cases ***
Validate successful Login
    Fill the login form

*** Keywords ***
Fill the login form
    Click Element     ${login-btn}
    Input Text        id:email       ${valid-username}
    Input Password    id:password    ${valid-password}
    Click Element     ${login-btn}
    Sleep             5s
    
