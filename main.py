import time
import requests

# DEFINE FUNCTION TO PROCESS EACH ENDPOINT
def process_endpoint(URL, ENDPOINT, DELAY, LOG_FILE):
    FULL_URL = URL + ENDPOINT
    print("Checking: " + FULL_URL)
    
    try:
        RESPONSE = requests.get(FULL_URL)
        # CHECK IF RESPONSE IS VALID (STATUS CODE BETWEEN 200 AND 399)
        if 200 <= RESPONSE.status_code < 400:
            LOG_FILE.write("Endpoint: " + ENDPOINT + "\n")
            LOG_FILE.write("URL: " + FULL_URL + "\n")
            LOG_FILE.write("Status code: " + str(RESPONSE.status_code) + "\n")
            LOG_FILE.write("\n")
            print("Status code: " + str(RESPONSE.status_code))
        else:
            print("Invalid response: " + str(RESPONSE.status_code))
    except requests.exceptions.RequestException as e:
        print("Error: " + str(e))
    
    time.sleep(DELAY)

# SET PARAMETERS
URL = "http://example.com/"
ENDPOINTS = ["api", "login", "admin", "users"]
DELAY = 1
LOG_FILE = open("log.txt", "w")

# PROCESS EACH ENDPOINT
for ENDPOINT in ENDPOINTS:
    process_endpoint(URL, ENDPOINT, DELAY, LOG_FILE)

# CLOSE LOG FILE
LOG_FILE.close()
