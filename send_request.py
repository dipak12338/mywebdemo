import requests 
import json

#url =  "http://127.0.0.1:5000/webhookcallback"
url =  "https://www.github.com/dipak12338/"

#url = 'http://127.0.0.1:5000/webhookcallback'
r = requests.post(url)
#print(r)
#print(r.content)

#data = { 'name': 'Ron', 'Course': 'Python'}

#r = requests.post(url, data=json.dumps(data), headers={'Content-Type' : 'application/json'})
print(r)

#### Get The Response On Same Page ####