# M-Pesa Daraja API Credentials (Sandbox)
# Replace these with your actual credentials from https://developer.safaricom.co.ke/

MPESA_CONSUMER_KEY = '0trhQlQxbCRFaZEWSPTKHY7yqSWcAAWjNP2JGQLb08KYgZa4'  
MPESA_CONSUMER_SECRET = '0guvMv8f5YYkMRoWYdUKOzfpFgwd4muiGnz9yAWyxZ4aWb10Jhh3LlsAzsSbBWE7'  
MPESA_SHORTCODE = '174379'  
MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' 

# API URLs
MPESA_BASE_URL = 'https://sandbox.safaricom.co.ke'
MPESA_ACCESS_TOKEN_URL = f'{MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials'
MPESA_STK_PUSH_URL = f'{MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest'
MPESA_STK_QUERY_URL = f'{MPESA_BASE_URL}/mpesa/stkpushquery/v1/query'