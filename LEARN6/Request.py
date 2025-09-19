import requests
response = requests.get('https://fairstrokes.com/')
print(f"My pastor says: {response.status_code} = Ask God for help and He will cause help to surround you status-(HTTP.status.code)")
print(response.text)