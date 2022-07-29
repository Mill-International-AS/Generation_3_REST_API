import time
import requests

IP_DEVICE = "192.168.8.151"

PROTOCOL_HTTP = "http://"
PROTOCOL_HTTPS = "https://"

ENDPOINT_STATUS = "/status"
ENDPOINT_SET_API_KEY = "/set-api-key"

AUTHENTICATION_KEY = "SeCrEt_K3Y"


# Product runs HTTP server - no authentication or encryption
url = PROTOCOL_HTTP + IP_DEVICE + ENDPOINT_STATUS
r = requests.get(url=url)
print(r.status_code)
print(r.text)

time.sleep(2)

# Product runs HTTP server - no authentication or encryption
url = PROTOCOL_HTTP + IP_DEVICE + ENDPOINT_SET_API_KEY
try:
    r = requests.post(url=url, json={"api_key": AUTHENTICATION_KEY}, timeout=5.0)
except requests.exceptions.ReadTimeout:
    print("Timeout on POST /set-api-key. Everything is all right")
    # There is no response because product needs to be restarted. After restart HTTPS server will be started.
    # Every request from now on will have to contain "Authentication" header with AUTHENTICATION_KEY as value
    # print(r.status_code)
    # print(r.text)
    pass
except Exception as e:
    print(f"Other error {e}")
    exit(1)

time.sleep(2)

url = PROTOCOL_HTTPS + IP_DEVICE + ENDPOINT_STATUS
r = requests.get(url=url, headers={"Authentication": AUTHENTICATION_KEY}, verify=False)
print(r.status_code)
print(r.text)


