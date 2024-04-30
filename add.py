base_url = 'https://petfriends.skillfactory.ru'
url_get = 'https://petfriends.skillfactory.ru/api/key'
url_pet_list= 'https://petfriends.skillfactory.ru/api/pets?filter=my_pets'
url_create_pet= 'https://petfriends.skillfactory.ru/api/create_pet_simple'
url_put = 'https://petfriends.skillfactory.ru/api/pets/1431cce9-878f-4586-aa79-e04179c631c4'
url_del = 'https://petfriends.skillfactory.ru/api/pets/149fb392-eaff-429d-a740-9aa6cd9efe04'
key = '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a'
password = 'test2022'
email = 'yaname.test@gmail.com'

headers_1 = {'email': email,'password': password,'accept': 'application/json'}

headers_put = {
    'accept': 'application/json',
    'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a',
    'Content-Type': 'application/json'
}

data_put  = {
    'name': 'Turbo',
    'animal_type': 'ulitka',
    'age': '5'
}
headers_3 = {'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a','accept': 'application/json'}

headers_post = {
    'accept': 'application/json',
    'auth_key': '7aaf89817fcebb6a9d441ca2e29b97b4b8142bc78a852bb18b16d65a',
    'Content-Type': 'application/json'
}

data_post  = {
    'name': 'Dandy',
    'animal_type': 'crokodile',
    'age': '3'
}
