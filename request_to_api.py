import requests
#test

response = requests.get('http://127.0.0.1:8000/job_listing/')
print(response.text)