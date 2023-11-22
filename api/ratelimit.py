import time

REQUEST_LIMIT = 100  # for example
WINDOW_SIZE = 60  # 60 seconds

request_counters = {}

def is_rate_limited(ip):
    current_time = time.time()
    window_start = current_time - WINDOW_SIZE
    
    if ip not in request_counters:
        request_counters[ip] = []
    
    # Filter out requests outside the current window
    request_counters[ip] = [timestamp for timestamp in request_counters[ip] if timestamp > window_start]
    
    if len(request_counters[ip]) < REQUEST_LIMIT:
        request_counters[ip].append(current_time)
        return False
    else:
        return True
