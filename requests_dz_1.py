import requests
TOKEN = 2619421814940190

Hulk = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
Hulk_id = Hulk.json()['results'][0]['id']

Captain_America = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain_America')
Captain_America_id = Captain_America.json()['results'][0]['id']

Thanos = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos')
Thanos_id = Thanos.json()['results'][0]['id']


H_powerstats = requests.get(f'https://superheroapi.com/api/2619421814940190/{Hulk_id}/powerstats')
H_int = int(H_powerstats.json()['intelligence'])

C_powerstats = requests.get(f'https://superheroapi.com/api/2619421814940190/{Captain_America_id}/powerstats')
C_int = int(C_powerstats.json()['intelligence'])

T_powerstats = requests.get(f'https://superheroapi.com/api/2619421814940190/{Thanos_id}/powerstats')
T_int = int(T_powerstats.json()['intelligence'])

id_list = (H_int, C_int, T_int)
max_id = max(id_list)
powerstats_list = (H_powerstats.json(), C_powerstats.json(), T_powerstats.json())
for i in powerstats_list:
    if int(i['intelligence']) == max_id:
        print('The most intelligent is', i['name'])
