#!/usr/bin/env python3
"""
API Test Keys and Client Examples
This file contains example API keys for testing purposes only.
All keys are fake and use low-entropy values for safety.
"""

import requests
import boto3
from datetime import datetime

# =============================================================================
# TEST API KEYS - DO NOT USE IN PRODUCTION
# =============================================================================

# AWS Keys
AWS_ACCESS_KEY_ID = "AKIATESTEXAMPLE123"
AWS_SECRET_ACCESS_KEY = "testSecretKey123456789012345678901234"
AWS_REGION = "us-west-2"

# Database Connections
DATABASE_URL = "postgresql://testuser:testpassword@localhost:5432/testdb"
REDIS_URL = "redis://testuser:testpassword@localhost:6379/0"
MONGODB_URI = "mongodb://testuser:testpassword@localhost:27017/testdb"

# API Keys for Various Services
OPENAI_API_KEY = "sk-test123456789012345678901234567890123456789012"
STRIPE_API_KEY = "sk_test_123456789012345678901234567890123456"
STRIPE_PUBLISHABLE_KEY = "pk_test_123456789012345678901234567890123456"
TWILIO_ACCOUNT_SID = "ACtest12345678901234567890123456789012"
TWILIO_AUTH_TOKEN = "testtoken12345678901234567890123456"
SENDGRID_API_KEY = "SG.testkey123456789.testkey123456789012345678901234567890"
MAILGUN_API_KEY = "key-test12345678901234567890123456789012"
GITHUB_TOKEN = "ghp_testtoken1234567890123456789012345678"
SLACK_BOT_TOKEN = "xoxb-test-123456789012-123456789012-testtoken123456789012"
DISCORD_BOT_TOKEN = "MTtesttoken.testtoken.testtoken123456789012345678901234"

# Cloud Service Keys
GOOGLE_CLOUD_API_KEY = "AIzaSyTestKey123456789012345678901234567"
AZURE_CLIENT_ID = "test-1234-5678-9012-123456789012"
AZURE_CLIENT_SECRET = "testSecret~123456789012345678901234567890"
HEROKU_API_KEY = "test-api-key-123456789012345678901234567890"

# Payment & Financial APIs
PAYPAL_CLIENT_ID = "ATestClientId123456789012345678901234567890123456789012"
PAYPAL_CLIENT_SECRET = "ETestSecret123456789012345678901234567890123456789012"
COINBASE_API_KEY = "testkey123456789012345678901234567890"
COINBASE_API_SECRET = "testsecret123456789012345678901234567890123456789012345="

# Social Media APIs
TWITTER_API_KEY = "testAPIKey123456789012345678901"
TWITTER_API_SECRET = "testAPISecret12345678901234567890123456789012345678901234"
FACEBOOK_APP_ID = "123456789012345"
FACEBOOK_APP_SECRET = "testsecret123456789012345678901234567890"

# =============================================================================
# CLIENT FUNCTIONS USING TEST KEYS
# =============================================================================

class TestAWSClient:
    """Example AWS client using test credentials"""
    
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
    
    def list_buckets(self):
        """List S3 buckets (will fail with test credentials)"""
        try:
            response = self.s3_client.list_buckets()
            return response['Buckets']
        except Exception as e:
            print(f"Expected error with test credentials: {e}")
            return []

class TestStripeClient:
    """Example Stripe client using test credentials"""
    
    def __init__(self):
        self.api_key = STRIPE_API_KEY
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    
    def create_customer(self, email):
        """Create a test customer"""
        url = "https://api.stripe.com/v1/customers"
        data = {'email': email}
        try:
            response = requests.post(url, headers=self.headers, data=data)
            return response.json()
        except Exception as e:
            print(f"Test API call failed as expected: {e}")
            return None

class TestOpenAIClient:
    """Example OpenAI client using test credentials"""
    
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def generate_text(self, prompt):
        """Generate text using OpenAI API"""
        url = "https://api.openai.com/v1/completions"
        data = {
            'model': 'text-davinci-003',
            'prompt': prompt,
            'max_tokens': 100
        }
        try:
            response = requests.post(url, headers=self.headers, json=data)
            return response.json()
        except Exception as e:
            print(f"Test API call failed as expected: {e}")
            return None

class TestTwilioClient:
    """Example Twilio client using test credentials"""
    
    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.base_url = f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}"
    
    def send_message(self, to_number, from_number, message):
        """Send SMS message"""
        url = f"{self.base_url}/Messages.json"
        data = {
            'To': to_number,
            'From': from_number,
            'Body': message
        }
        try:
            response = requests.post(
                url, 
                data=data, 
                auth=(self.account_sid, self.auth_token)
            )
            return response.json()
        except Exception as e:
            print(f"Test API call failed as expected: {e}")
            return None

class TestGitHubClient:
    """Example GitHub client using test credentials"""
    
    def __init__(self):
        self.token = GITHUB_TOKEN
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    
    def get_user_repos(self, username):
        """Get user repositories"""
        url = f"https://api.github.com/users/{username}/repos"
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            print(f"Test API call failed as expected: {e}")
            return []

class TestSlackClient:
    """Example Slack client using test credentials"""
    
    def __init__(self):
        self.token = SLACK_BOT_TOKEN
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    def post_message(self, channel, text):
        """Post message to Slack channel"""
        url = "https://slack.com/api/chat.postMessage"
        data = {
            'channel': channel,
            'text': text
        }
        try:
            response = requests.post(url, headers=self.headers, json=data)
            return response.json()
        except Exception as e:
            print(f"Test API call failed as expected: {e}")
            return None

def test_database_connections():
    """Test database connection strings"""
    print("Testing database connections with test credentials:")
    print(f"PostgreSQL: {DATABASE_URL}")
    print(f"Redis: {REDIS_URL}")
    print(f"MongoDB: {MONGODB_URI}")
    print("Note: These are test credentials and will not work in production")

def main():
    """Demonstrate usage of test API clients"""
    print("=== API Test Client Examples ===")
    print(f"Timestamp: {datetime.now()}")
    print()
    
    # Test AWS Client
    print("1. Testing AWS Client:")
    aws_client = TestAWSClient()
    aws_client.list_buckets()
    print()
    
    # Test Stripe Client
    print("2. Testing Stripe Client:")
    stripe_client = TestStripeClient()
    stripe_client.create_customer("test@example.com")
    print()
    
    # Test OpenAI Client
    print("3. Testing OpenAI Client:")
    openai_client = TestOpenAIClient()
    openai_client.generate_text("Hello, this is a test prompt")
    print()
    
    # Test Twilio Client
    print("4. Testing Twilio Client:")
    twilio_client = TestTwilioClient()
    twilio_client.send_message("+1234567890", "+0987654321", "Test message")
    print()
    
    # Test GitHub Client
    print("5. Testing GitHub Client:")
    github_client = TestGitHubClient()
    github_client.get_user_repos("octocat")
    print()
    
    # Test Slack Client
    print("6. Testing Slack Client:")
    slack_client = TestSlackClient()
    slack_client.post_message("#general", "Hello from test bot!")
    print()
    
    # Test Database Connections
    print("7. Database Connection Strings:")
    test_database_connections()
    print()
    
    print("=== All tests completed ===")
    print("Remember: All credentials used are for testing only!")

if __name__ == "__main__":
    main()