import requests

numeroApt = input('Apartamento: ')
print('Informado:',numeroApt)

payload = {'id': '123ABC', 'apartamento': numeroApt}
r = requests.get('http://127.0.0.1:5000/api/notificar',params=payload)
