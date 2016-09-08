import requests

response = requests.post("http://ccid-eddieantonio.rhcloud.com/easantos")

print response.status_code
