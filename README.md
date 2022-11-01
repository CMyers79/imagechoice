# imagechoice
Microservice for CS361
Communication Contract:

Calling service must send GET request to https://imagechoice.herokuapp.com/imagechoiceapp/quantity,
where quantity is the maximum of the range of random integers to be generated.  The random integer in the response 
will be between 1 and quantity.

The repsonse will be a JSON in the following format:

{"status" : string, "data" : integer or string}

The status string will be either "sucess" or "error", and the data field will contain either the random integer, or an error message.

The following example code shows how to request, recieve, and access the random integer:

CODE:
import requests


url = "http://imagechoice.herokuapp.com/imagechoiceapp/10"
response = requests.get(url)
print("GET request received response:")
print(response.text)

data = response.json()
print(data)

number = data["data"]
print(number)

OUTTPUT:
GET request received response:
{"status":"success","data":8}
{'status': 'success', 'data': 8}
8

![Untitled Diagram](https://user-images.githubusercontent.com/30599967/199170437-ac8a6982-9d80-4408-921f-35ea54b3deb8.jpg)
