import requests
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


URL = "https://random-data-api.com/api/color/random_color"

'''
{
    'id': 7927, 'uid': 'b5053ecf-4157-4393-9656-121ba36f3c02', 
    'hex_value': '#569062', 'color_name': 'harlequin', 
    'hsl_value': [358, 0.91, 0.34], 'hsla_value': [338, 0.34, 0.49, 0.4]
}
'''

class RandomData:
    def __init__(self,id,uid,hex_value,color_name, hsl_value,hsla_value):
        self.id = id
        self.uid = uid
        self.hex_value = hex_value
        self.color_name = color_name
        self.hsl_value = hsl_value
        self.hsla_value = hsla_value


count = 0

while True:

    r = requests.get(URL)
    page = r.json()

    count += 1
    for x in range(0,10000,10):
        if count == x:
            print(f"Data fetched {count} times! ")

    RandomData.id = page["id"]
    RandomData.uid = page["uid"]
    RandomData.hex_value = page["hex_value"]
    RandomData.color_name = page["color_name"]
    RandomData.hsl_value = page["hsl_value"]
    RandomData.hsla_value = page["hsla_value"]

    print(
    f"""
    ************************************
    * ID: {RandomData.id} \r
    * UID: {RandomData.uid}
    * Hex Value: {RandomData.hex_value}
    * Color Name: {RandomData.color_name}
    * HSL Value: {RandomData.hsl_value}
    * HSLA Value: {RandomData.hsla_value}
    ************************************
    """
    
    )
    time.sleep(1)
