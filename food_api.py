import json
import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

food_url = "https://foodish-api.herokuapp.com/api/"

def get_food_data():
    #Get response from website
    response = urllib.request.urlopen(food_url)


    #convert from Json to Python
    json_data = response.read()
    python_data = json.loads(json_data)

    return python_data

food_image = get_food_data()
image = food_image["image"]

urllib.request.urlretrieve(image, "image.jpg")
