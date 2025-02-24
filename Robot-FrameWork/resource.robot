*** Settings ***
Documentation    A resource file with reusable Keyword and Variables
Library          SeleniumLibrary

*** Variables ***
${login-btn} =             id:login-btn
${valid-username} =        gandhamathan@guvi.in
${valid-password} =        Gandha9499@
*** Keywords ***
 Open the browser with the Guvi url
     Create Webdriver    Chrome
     Go To               https://www.guvi.in/
     Maximize Browser Window
    