import urllib.request
import json
from datetime import datetime
import time
iss_url = "http://api.open-notify.org/iss-now"

def get_iss_data():
    #Get response from website
    response = urllib.request.urlopen(iss_url)


    #convert from Json to Python
    json_data = response.read()
    python_data = json.loads(json_data)

    return python_data
iss_data = get_iss_data()

position = iss_data["iss_position"]
timestamp = iss_data["timestamp"]

for repeat in range(10):
    print(f"the longitude of the ISS is {position['longitude']}")
    print(f"the latitude of the ISS is {position['latitude']}")
    print(f"the timestamp is {datetime.fromtimestamp(timestamp)}")
    time.sleep(3)
