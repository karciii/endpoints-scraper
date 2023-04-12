import time
import requests
import yaml

class EndpointChecker:
    def __init__(self, base_url, endpoints, delay, log_file):
        self.base_url = base_url
        self.endpoints = endpoints
        self.delay = delay
        self.log_file = log_file
    
    def process_endpoint(self, endpoint):
        full_url = self.base_url + endpoint
        print("Checking: " + full_url)
        
        try:
            response = requests.get(full_url)
            # check if response is valid (status code between 200 and 399)
            if 200 <= response.status_code < 500:
                self.log_file.write("Endpoint: " + endpoint + "\n")
                self.log_file.write("URL: " + full_url + "\n")
                self.log_file.write("Status code: " + str(response.status_code) + "\n")
                self.log_file.write("\n")
                print("Status code: " + str(response.status_code))
            else:
                print("Invalid response: " + str(response.status_code))
        except requests.exceptions.RequestException as e:
            print("Error: " + str(e))
        
        time.sleep(self.delay)

    def check_all_endpoints(self):
        for endpoint in self.endpoints:
            self.process_endpoint(endpoint)

        # Close log file
        self.log_file.close()

# open yaml file
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# get parameters from config file
base_url = config["settings"]["base_url"]
endpoints = config["settings"]["endpoints"]
delay = config["settings"]["delay"]
log_file = config["settings"]["log_file_name"]


# set parameters
# base_url = "http://example.com/"
# endpoints = ["api", "login", "admin", "users"]
# delay = 1
log_file = open("log.txt", "w")

# Create an instance of EndpointChecker and call the check_all_endpoints method
checker = EndpointChecker(base_url, endpoints, delay, log_file)
checker.check_all_endpoints()
