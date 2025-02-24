*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary  

*** Test Cases ***
Validate successful Login
    Open the browser with the Guvi URL
    Enter the details
    Wait untill it checks and display error message
    Verify the error message
    

*** Keywords ***
Open the browser with the Guvi URL
    Create Webdriver    Chrome
    Go To               https://www.guvi.in/sign-in/
    
Enter the details
    Input Text        Xpath://input[@id='email']       gandhamathan@guvi.in
    Input Password    Xpath://input[@id='password']    sfsadfs
    Click Element      id://a[@id='login-btn']
    
Wait untill it checks and display error message
    Wait Until Element Is Visible    css:.invalid-feedback

Verify the error message
    ${result}=     Get Text    css:.invalid-feedback
    Should Be Equal As Strings    ${result}    Incorrect Email or Password

