"""
Scanning Endpoints based on URL
"""

import time
import requests

URL = "http://example.com/"

# Endpoints list
endpoints = ["api", "login", "admin", "users"]

# delay time between queries in secconds  
DELAY = 1

# log file
LOG_FILE = open("log.txt", "w")

for endpoint in endpoints:
    # generating full enpoint url
    FULL_URL = URL + endpoint
    
    print("Checking: " + FULL_URL)
    
    # Wysyłanie zapytania HTTP GET do adresu URL
    response = requests.get(FULL_URL)
    
    # Writing response to log file
    LOG_FILE.write("Endpoint: " + endpoint + "\n")
    LOG_FILE.write("URL: " + FULL_URL + "\n")
    LOG_FILE.write("Status code: " + str(response.status_code) + "\n")
    LOG_FILE.write("\n")
    
    # Wyświetlanie odpowiedzi na konsoli
    print("Status code: " + str(response.status_code))
    print()
    
    # delay wait
    time.sleep(DELAY)

# closing log file
LOG_FILE.close()
