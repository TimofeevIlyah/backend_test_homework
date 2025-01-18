import requests

responce = requests.get('http://info.cern.ch')

print(responce.text)
