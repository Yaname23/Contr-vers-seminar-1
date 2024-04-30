import requests
import json

from api import headers_1, url_pet_list, url_get, url_del, headers_3, url_create_pet, headers_post, data_post, url_put, data_put, headers_put

for url in [url_get]:
    res = requests.get(url_get, headers= headers_1)
    if res.status_code == 200:
        print('GET.Статус код: 200.', 'API-ключ: ', res.json())
    else:
        print('GET.Код ошибки:',res.status_code)
for url in [url_pet_list]:
    r = requests.get(url_pet_list, headers=headers_3)
    if r.status_code == 200:
        print('GET.Статус код: 200.', 'Список моих животных: ', r.json())
    else:
        print('GET.Код ошибки:',r.status_code)

for url in [url_create_pet]:
    a = requests.post(url_create_pet, headers=headers_post, data=json.dumps(data_post))
    if a.status_code == 200:
        print('POST.Статус код: 200.','Добавлены данные:', data_post)
    else:
        print('POST.Код ошибки:',a.status_code, '.Новые данные не были добавлены')
for url in [url_put]:
    pu = requests.put(url, headers=headers_put, data=json.dumps(data_put))
    if pu.status_code == 200:
        print('PUT.Статус код: 200.','Изменен возраст Турбо, обновленные данные:',pu.text )
    else:
        print('PUT.Код ошибки: ', pu.status_code, ', данные не были изменены')
for url in [url_del]:
    re = requests.delete(url_del, headers=headers_3)
    if re.status_code == 200:
        print('DELETE.Статус код: 200.','Удаление питомца прошло успешно')
    else:
        print('DELETE.Код ошибки: ', re.status_code, ', удаление питомца не было произведено')
