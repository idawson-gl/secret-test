#!/bin/bash

# Function to read password securely (without echoing to terminal)
read_password() {
    echo -n "Password: "
    read -s password
    echo  # Add newline after password input
}

# Get credentials from environment variables or prompt user
if [[ -n "$AUTH_USERNAME" && -n "$AUTH_PASSWORD" ]]; then
    echo "Using credentials from environment variables..."
    username="$AUTH_USERNAME"
    password="$AUTH_PASSWORD"
else
    echo "Environment variables AUTH_USERNAME and AUTH_PASSWORD not found."
    echo "Please enter credentials manually:"
    
    # Read username
    echo -n "Username: "
    read username
    
    # Read password securely
    read_password
fi

# Combine username and password with colon separator
credentials="${username}:${password}"

# Base64 encode the credentials
encoded_credentials=$(echo -n "$credentials" | base64)

# Send curl request with Authorization header
echo "Sending request to example.com..."
curl -H "Authorization: Basic $encoded_credentials" \
     -H "Content-Type: application/json" \
     -X GET \
     https://example.com/api/endpoint

# Clear sensitive variables
unset username
unset password
unset credentials
unset encoded_credentials

echo "Request completed."