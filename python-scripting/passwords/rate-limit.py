import time

# Dictionary to store the number of requests from each IP address
request_count = {}

# Rate limiting function
def rate_limit(ip_address, max_requests, time_frame):
    current_time = int(time.time())
    
    # Remove expired entries
    expired_ips = [ip for ip, (timestamp, count) in request_count.items() if current_time - timestamp > time_frame]
    for ip in expired_ips:
        del request_count[ip]
    
    # Check if IP address is already in the dictionary
    if ip_address in request_count:
        timestamp, count = request_count[ip_address]
        
        # Update request count if within time frame
        if current_time - timestamp < time_frame:
            count += 1
        else:
            count = 1
        request_count[ip_address] = (current_time, count)
    else:
        request_count[ip_address] = (current_time, 1)
    
    # Check if request count exceeds the limit
    if request_count[ip_address][1] > max_requests:
        return False
    else:
        return True

if __name__ == "__main__":
    # Test rate limiting
    ip_address = "192.168.1.1"
    max_requests = 5
    time_frame = 60  # 1 minute in seconds
    
    for _ in range(7):  # Send 7 requests
        if rate_limit(ip_address, max_requests, time_frame):
            print("Request allowed.")
        else:
            print("Rate limit exceeded. Please try again later.")
            break
