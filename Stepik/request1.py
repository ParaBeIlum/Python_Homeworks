import requests

URL = 'https://stepic.org/media/attachments/course67/3.6.3/'
name = '699991.txt'
while name[:2] != 'We':
    name = requests.get(URL + name).text
    print(name)
print(name)