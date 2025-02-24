import requests
import re

def postrequest(url,headers,payload):
    response = requests.request("POST", url, headers=headers, data=payload) 
    if response.status_code == 200:
        # print("Response",response.text)
        return response.text
    else:
        print("error")
        raise

# this method used to fetch the value 
def fetch_and_validate(response_text, key, expected_value=None):
    """Extracts a specific value from response text, cleans it, and validates it."""
    try:
        # Extract the value from the response text
        value = response_text.split(f'"{key}":')[1].split(",")[0].replace('"', '').strip()
        
        # Clean the extracted value (remove unwanted characters)
        cleaned_value = re.sub(r'[^a-zA-Z0-9-_]', '', value)
        
        # Validate against expected value (if provided)
        if expected_value and cleaned_value != expected_value:
            return f"Validation Failed: Expected '{expected_value}', but got '{cleaned_value}'"
        
        return cleaned_value  # Return the cleaned value if validation passes
    

    except (IndexError, AttributeError):
        # raise
        return f"Key '{key}' not found in response"
        
    
