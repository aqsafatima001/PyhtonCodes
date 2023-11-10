import requests

url = "https://mycookbook-io1.p.rapidapi.com/recipes/rapidapi"

payload = "https://www.jamieoliver.com/recipes/vegetables-recipes/superfood-salad/"
headers = {
	"content-type": "text/plain",
	"X-RapidAPI-Key": "a316acff38msh92b00c304d61038p1beba1jsnffa9caee5063",
	"X-RapidAPI-Host": "mycookbook-io1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)