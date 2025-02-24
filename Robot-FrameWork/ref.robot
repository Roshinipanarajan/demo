*** Settings ***
Documentation    To Validate the login Page
Library          SeleniumLibrary

*** Test Cases ***
Validate successful Login
    Open the browser with the Guvi url
    Fill the login form

*** Keywords ***
 Open the browser with the Guvi url
     Create Webdriver    Chrome
     Go To               https://www.guvi.in/
     Maximize Browser Window

Fill the login form
    Click Element     id:login-btn
    Input Text        id:email       gandhamathan@guvi.in
    Input Password    id:password    Gandha9499@
    Click Element     id:login-btn 
