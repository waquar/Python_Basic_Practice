import requests

r = requests.get('https://financialmodelingprep.com/api/v3/company/profile/AAPL')    #get gets the result from url
print(r.text)      #returns data in text
print(r.status_code)

url = 'xyz'
data = {'p1': 4 , 'p2': 8}
r2 = requests.post(url = url, data = data )


