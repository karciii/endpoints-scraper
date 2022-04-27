import requests

url = 'https://reqbin.com/echo'

x = requests.get(url)

print(x.text)