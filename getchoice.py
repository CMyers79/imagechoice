import requests


url = "http://imagechoice.herokuapp.com/imagechoiceapp/10"
response = requests.get(url)
print("GET request received response:")
print(response.text)
