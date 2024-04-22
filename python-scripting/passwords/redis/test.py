import redis

# Connect to Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def rate_limit_with_redis(ip_address, max_requests, time_frame):
    key = f"rate_limit:{ip_address}"
    
    # Increment the counter for the IP address
    current_count = r.incr(key)
    
    # Set expiration if the key is new
    if current_count == 1:
        r.expire(key, time_frame)
    
    # Check if request count exceeds the limit
    if current_count > max_requests:
        return False
    else:
        return True

if __name__ == "__main__":
    # Test rate limiting
    ip_address = "192.168.1.1"
    max_requests = 5
    time_frame = 60  # 1 minute in seconds
    
    for _ in range(7):  # Send 7 requests
        if rate_limit_with_redis(ip_address, max_requests, time_frame):
            print("Request allowed.")
        else:
            print("Rate limit exceeded. Please try again later.")
            break
