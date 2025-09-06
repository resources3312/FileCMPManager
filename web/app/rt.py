import requests



print(requests.post("http://127.0.0.1/services/filepair/cmp"), files={'file_1': open('./config.py'), 'file_2': open('./config.py')}, cookies={'token': '1'})

